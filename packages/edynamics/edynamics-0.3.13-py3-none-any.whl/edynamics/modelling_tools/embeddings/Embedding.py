import numpy as np
import pandas as pd
import logging

from typing import List
from scipy.spatial import cKDTree
from edynamics.modelling_tools.observers import Observer


class Embedding:
    def __init__(
        self, data: pd.DataFrame, observers: List[Observer], library_times: pd.DatetimeIndex, compile_block: bool
    ):
        """
        Defines a state space Embedding of generic observer functions from a set of data.

        :param pd.DataFrame data: data to be embedded.
        :param observers: Observation functions for the Embedding.
        :param bool compile_block: If true, compile the embedding block by applying observer functions to the data
        """

        self.data = data
        self.observers = observers
        self.library_times = library_times

        #: pd.DatetimeIndex.Freq the frequency spacing of the time series
        self.frequency = data.index.freq
        #: int: dimension of the Embedding, equal to the length of the list of observation functions.
        self.dimension: int = len(observers)
        #: scipy.spatial.cKDTree: a KDTree storing the distances between all pairs of library points for the delay
        # Embedding using the l2 Norm in R^n where n is the Embedding dimension (i.e. number of lags, len(self.lags))
        self.distance_tree = None
        #: pd.DataFrame: pandas dataframe of the delay Embedding
        self.block = None

        if compile_block:
            self.compile()

        logging.info("Embedding created.")

    # PUBLIC
    def compile(self) -> None:
        """
        Builds the Embedding block according to the observations functions.
        """

        logging.info(msg="Compiling the state space...")

        self.block = pd.DataFrame(
            columns=[obs.observation_name for obs in self.observers],
            index=self.library_times,
        )

        # build the Embedding block
        for obs in self.observers:
            self.block[obs.observation_name] = [obs.observe(self.data, time) for time in self.library_times]

        self.block.dropna(inplace=True)

        # build the KDTree
        self.distance_tree = cKDTree(self.block.iloc[:-1])

        logging.info(msg="State space compiled.")

    def get_points(self, times: pd.DatetimeIndex) -> pd.DataFrame:
        """
        Retrieves the embedded state space points for a given set of times.

        :param pd.DatetimeIndex times: the index of times for the desired points
        """

        logging.debug("Getting embedded point at times: {}".format(times))
        if self.observers is None:
            return self.data.loc[times]

        points = pd.DataFrame(
            index=times,
            columns=[obs.observation_name for obs in self.observers],
            dtype=float,
        )

        for time in times:
            for obs in self.observers:
                points.loc[time, obs.observation_name] = obs.observe(self.data, time)

        return points

    def set_library(self, library_times: pd.DatetimeIndex) -> None:
        self.library_times = library_times

    def get_k_nearest_neighbours(
        self, point: np.array, max_time: pd.Timestamp, knn: int
    ) -> List[int]:
        """
        Returns the k nearest neighbours of the Embedding and their distances to the given embedded point The time
        index of the neighbours is less than the given maximum time.

        :param np.array point: the point for which we want the k nearest neighbours. The point should be a vector, i.e.
        a 1-D np.array.
        :param pd.Timestamp max_time: the time for which all k nearest neighbour times need to be less than.
        :param int knn: the number of nearest neighbours to return.
        :return: a list of the integer indices of the k nearest neighbours in the library block.
        """

        logging.debug("Getting k nearest neighbours of: {}".format(point))
        knn_idxs = np.empty(shape=knn, dtype=int)
        count = 0
        k = list(range(1, knn + 1))
        while count < knn:
            dists, knn_idxs = self.distance_tree.query(point, k)
            for idx in knn_idxs:
                if self.block.index[idx] <= max_time:
                    knn_idxs[count] = idx

                    count += 1

            k = [k[-1] + 1]

        return knn_idxs
