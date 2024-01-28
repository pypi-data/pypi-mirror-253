import __local__
from luma.classifier.svm import KernelSVC
from luma.ensemble.forest import RandomForestClassifier
from luma.classifier.logistic import SoftmaxRegressor
from luma.visual.evaluation import ValidationHeatmap

from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
import numpy as np


X, y = load_wine(return_X_y=True)
X = X[:, [6, 9]]

param_dict = {'n_trees': [10, 20, 50, 100],
              'max_depth': [5, 10, 50, 100]}

valid_hmap = ValidationHeatmap(RandomForestClassifier(), 
                               X, y, 
                               param_dict=param_dict, 
                               random_state=42,
                               verbose=True)

valid_hmap.plot(show=True)
