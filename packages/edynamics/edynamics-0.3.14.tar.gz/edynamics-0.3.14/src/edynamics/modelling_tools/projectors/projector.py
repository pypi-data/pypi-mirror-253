import abc

import pandas as pd

from edynamics.modelling_tools.embeddings import Embedding
from edynamics.modelling_tools.kernels import Kernel
from edynamics.modelling_tools.norms import Norm


class Projector(abc.ABC):
    def __init__(self, norm: Norm, kernel: Kernel):
        """
        Abstract class defining state space based prediction strategies.

        :param norm: which vector Norm to use.
        :param kernel: which weighting kernel to use.
        """
        self.norm = norm
        self.kernel = kernel

    @abc.abstractmethod
    def project(
            self, embedding: Embedding, points: pd.DataFrame, steps: int, step_size: int, leave_out: bool
    ) -> pd.DataFrame:
        """
        Abstract method defining state spaced based prediction methods for predictions of delay Embedding points
        :param embedding: the state space Embedding.
        :param points: the points to be projected.
        :param steps: the number of prediction steps to make out from for each point. By default 1.
        period.
        :param step_size: the number to steps, of length given by the frequency of the block, to prediction.
        :return: the projected points.
        """
        raise NotImplementedError

    @staticmethod
    def update_values(
            embedding: Embedding,
            predictions: pd.DataFrame,
            current_time: pd.DatetimeIndex,
            prediction_time: pd.DatetimeIndex,
    ) -> pd.DataFrame:
        """
        Updates a given predicted point in a predicted DATA block by replacing the variables with either the
        actual variables, if available, or the projected variables from previous predictions.
        :return: the updated dataframe of projections.
        """
        for obs in embedding.observers:
            # Get the times needed to make an observation for this observer at this prediction time
            obs_times = obs.observation_times(
                frequency=embedding.frequency, time=prediction_time
            )

            unobserved = [time for time in obs_times if time > current_time]
            observed = [time for time in obs_times if time <= current_time]

            try:
                data = pd.concat(
                    [
                        predictions.loc[current_time].loc[unobserved][obs.variable_name],
                        embedding.data.loc[observed][obs.variable_name],
                    ]
                ).to_frame()
            except KeyError as e:
                if any(a not in predictions.loc[current_time].index for a in unobserved):
                    offenders = [a for a in unobserved if a not in predictions.loc[current_time].index]
                    print(f"The times {offenders} used to make observation {obs.observation_name} at time "
                          f"{prediction_time} are not in the observed or previously predicted values. The step_size"
                          f" likely exceeds the an observation lag size.")
                    print(e)

            data.sort_index(inplace=True)
            hit = False

            if data.index.inferred_freq is not None:
                data.index.freq = data.index.inferred_freq
            else:
                data.index.freq = embedding.frequency

            predictions.loc[(current_time, prediction_time)][
                obs.observation_name
            ] = obs.observe(data=data, times=pd.DatetimeIndex(data=[prediction_time])).values

        return predictions

    @staticmethod
    def build_prediction_index(
            frequency: pd.DatetimeIndex.freq, index: pd.Index, steps: int, step_size: int
    ) -> pd.MultiIndex:
        """
        :param frequency: the frequency denoting the time span between predictions.
        :param index: the index of times from which to make predictions
        :param steps: the number of prediction steps to make out from for each time. By default 1.
        :param step_size: the number to steps, of length given by the frequency of the block, to prediction.
        :return pd.MultiIndex: multi index of points where the first index is the starting point for each multi step
        prediction which are given in the second index. E.g. index (t_4, t_10) is the prediction of t_10 made on a
        multistep prediction starting at t_4.
        """
        tuples = list(
            zip(
                index.repeat(repeats=steps),
                # todo: this doesn't work in the degenerative case where step_size = 0
                sum(
                    zip(*[index + frequency * (step_size + i) for i in range(steps)]),
                    (),
                ),
            )
        )

        return pd.MultiIndex.from_tuples(
            tuples=tuples, names=["Current_Time", "Prediction_Time"]
        )

    def __eq__(self, other):
        if isinstance(other, Projector):
            return self.norm == other.norm and self.kernel == other.kernel
        return False
