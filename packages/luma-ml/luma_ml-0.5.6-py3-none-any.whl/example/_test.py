import __local__
from luma.model_selection.robust import RANSAC, MLESAC
from luma.regressor.poly import PolynomialRegressor
from luma.visual.result import ResidualPlot

import matplotlib.pyplot as plt
import numpy as np


np.random.seed(10)
X = np.linspace(-3, 3, 1000)
y = X ** 3

indices = np.arange(650, 800)
y[indices] = -10 * X[indices]
y += np.random.normal(0, 1.5, 1000)
X = X.reshape(-1, 1)

model = MLESAC(estimator=PolynomialRegressor(degree=3),
               min_points=2,
               max_iter=1000,
               min_inliers=0.5,
               threshold=None,
               random_state=10)

model.fit(X, y)

coef = model.best_estimator.coefficients
func = f"({coef[2]:.3f}){r'$x^3$'}+({coef[1]:.3f}){r'$x^2$'}+({coef[0]:.3f}){r'$x$'}"

res = ResidualPlot(estimator=model,
                   X=X,
                   y=y)

res.plot(show=True)
