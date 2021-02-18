from linear_cost import linear_cost, linear_cost_gradient
from gradient_descent import gradient_descent
import numpy as np

TRAINING_SET_SIZE = 200
x = np.linspace(-10, 30, TRAINING_SET_SIZE)
X = np.vstack(
    (
        np.ones(TRAINING_SET_SIZE),
        x
    )
).T

y = (5 + 2 * x + np.random.randint(-15, 15, TRAINING_SET_SIZE)).reshape(
    TRAINING_SET_SIZE,
    1
)

m, n = X.shape
theta_0 = np.random.rand(n, 1)
r_theta, costs = gradient_descent(
    X,
    y,
    theta_0,
    linear_cost,
    linear_cost_gradient
)