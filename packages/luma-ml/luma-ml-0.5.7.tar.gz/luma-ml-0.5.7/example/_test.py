import __local__
from luma.classifier.svm import KernelSVC
from luma.visual.evaluation import ValidationHeatmap

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np


X, y = load_iris(return_X_y=True)
X = X[:100]
y = y[:100]

param_dict = {'C': np.logspace(-4, 4, 10),
              'gamma': np.logspace(-4, 2, 10)}

valid_hmap = ValidationHeatmap(KernelSVC(), X, y, 
                               param_dict=param_dict, 
                               random_state=42)

valid_hmap.plot(log_xscale=True,
                log_yscale=True,
                annotate=False,
                show=True)
