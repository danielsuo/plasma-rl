import os
import jax.numpy as np
import pandas as pd
from keras.models import load_model

import tigerforecast
from tigerforecast.utils.dataset_registry import dataset_to_problem, get_tigerforecast_dir
from tigerforecast.error import StepOutOfBounds
from tigerforecast.problems import Problem
from tigerforecast.methods import Method


class PlasmaProblem(Problem):
    """
    Description: Demo with data from

    Kates-Harbeck, Julian & Svyatkovskiy, Alexey & Tang, William. (2019). Predicting disruptive instabilities in controlled fusion plasmas through deep learning. Nature. 568. 10.1038/s41586-019-1116-4. 
    """

    compatibles = set(["TimeSeries"])

    def __init__(self):
        self.initialized = False
        self.has_regressors = False

    def initialize(self, path, shot_number):
        """
        Description: initialization
        Args:
            path (string): path to shot data
            shot_number (int): shot number to use
        """

        self.data = np.load(path, allow_pickle=True)
        self.data = self.data["shot_data"].item()
        self.shot_number = shot_number

        print("shot_number,X.shape,is_disruptive,disruption_time")
        for k in self.data.keys():
            print(k, self.data[k]["X"].shape, self.data[k]["is_disruptive"],
                  self.data[k]["disruption_time"])

        # Just hold onto shot_number for now
        self.data = self.data[shot_number]

        self.T = 0
        self.initialized = True

    def step(self):
        if self.T == self.data["X"].shape[0]:
            raise StepOutOfBounds(
                "Number of steps exceeded length of dataset ({})".format(
                    self.data["X"].shape[0]))

        ret = self.data["X"][self.T, :]

        self.T += 1

    def hidden(self):
        pass

    def close(self):
        pass

    def __str__(self):
        return "<Plasma Problem>"


class FRNNMethod(Method):
    """
    Description: FRNN
    """

    compatibles = set(['TimeSeries'])

    def __init__(self):
        self.initialized = False
        self.use_regressors = False

    def initialize(self, path):
        self.model = load_model(path)
        self.model.summary()

    def predict(self, x):
        return self.model.predict(x)

    def forecast(self, x, timeline=1):
        pass

    def update(self, y):
        pass

    def __str__(self):
        return "<FRNN Method>"
