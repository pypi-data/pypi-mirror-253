import numpy as np
import pandas as pd

from scipy.spatial import cKDTree

from edynamics.modelling_tools.observers import observer


class embedding:
    def __init__(self,
                 data: pd.DataFrame,
                 observers: [observer],
                 library_times: [pd.Timestamp]
                 ):
        """
        Defines a state space embedding of generic observer functions from a set of data.

        :param pd.DataFrame data: data to be embedded.
        :param [observer] observers: list of observation functions for the embedding
        :param pd.Timestamp library_times: the set of times determining the embedding library.
        :param Callable[pd.Timestamp, Callable] mask: a function that, taking a pandas timestamp, returns a function
            that can be used to filter the block for observations of the given timestamp type.
        """

        self.data = data
        self.observers = observers
        self.library_times = library_times

        #: the frequency spacing of the time series
        self.frequency = data.index.freq
        #: pd.DataFrame: pandas dataframe of the delay embedding
        self.block: pd.DataFrame = None
        #: int: dimension of the embedding, equal to the length of the list of observation functions.
        self.dimension: int = len(observers)
        #: scipy.spatial.cKDTree: a KDTree storing the distances between all pairs of library points for the delay
        # embedding using the l2 norm in R^n where n is the embedding dimension (i.e. number of lags, len(self.lags))
        self.distance_tree: cKDTree = None

    # PUBLIC
    def compile(self) -> None:
        """
        Builds the embedding block according to the observations functions.
        """

        self.block = pd.DataFrame(columns=[obs.observation_name for obs in self.observers], index=self.library_times)

        # build the embedding block
        for obs in self.observers:
            obs_data = list(map(obs.observe, [self.data for _ in range(len(self.library_times))], self.library_times))

            self.block[obs.observation_name] = obs_data

        self.dimension = len(self.observers)
        self.block.dropna(inplace=True)

        # build the KDTree
        self.distance_tree = cKDTree(self.block.iloc[:-1])

    def get_points(self,
                   times: [pd.Timestamp]) -> pd.DataFrame:
        """
        Retrieves the embedded state space points for a given set of times.

        :param [pd.Timestamp] times: the index of times for the desired points
        """

        if self.observers is None:
            return self.data.loc[times]

        points = pd.DataFrame(index=times,
                              columns=[obs.observation_name for obs in self.observers],
                              dtype=float)

        for time in times:
            for obs in self.observers:
                points.loc[time, obs.observation_name] = obs.observe(self.data, time)

        return points

    def set_library(self,
                    library_times: [pd.Timestamp]):

        self.library_times = library_times

    def get_k_nearest_neighbours(self,
                                 point: np.array,
                                 max_time: pd.Timestamp,
                                 knn: int) -> [int]:
        """
        Returns the k nearest neighbours of the embedding and their distances to the given embedded point The time
        index of the neighbours is less than the given maximum time.

        :param np.array point: the point for which we want the k nearest neighbours. The point should be a vector, i.e.
        a 1-D np.array.
        :param pd.Timestamp max_time: the time for which all k nearest neighbour times need to be less than.
        :param int knn: the number of nearest neighbours to return.
        :return: a list of the integer indices of the k nearest neighbours in the library block.
        """
        knn_idxs = np.empty(shape=knn, dtype=int)
        count = 0
        k = list(range(1, knn + 1))
        while count < knn:
            dists, knn_idxs = self.distance_tree.query(point, k)
            for idx in knn_idxs:
                if self.block.index[idx] <= max_time:
                    knn_idxs[count] = idx

                    count += 1

            # todo: wtf is this?
            k = [k[-1] + 1]

        return knn_idxs
