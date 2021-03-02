import numpy as np
import matplotlib.pyplot as plt
from linear_cost import linear_cost, linear_cost_gradient

TRAINING_SET_SIZE = 200

x = np.linspace(-10, 30, TRAINING_SET_SIZE)

X = np.vstack(
    (
        np.ones(TRAINING_SET_SIZE),
        x,
        x**2,
        x/**3
    )
).T

y = (5 + 2 * x ** 3 + np.random.randint(-200, 200, TRAINING_SET_SIZE)).reshape(
    TRAINING_SET_SIZE,
    1
)

m, n = X.shape

theta_0 = np.random.rand(n, 1)


# plt.scatter(X[:,1], y)
# plt.show()

def gradient_descent(
    x,
    y,
    theta_0,
    cost_function,
    cost_function_gradient,
    learning_rate=0.000001,
    threshold=2,
    max_iter=1000
):
    theta = theta_0
    iteration = 0
    costs = []

    while np.linalg.norm(cost_function_gradient(x, y, theta)) > threshold and iteration < max_iter:
        iteration += 1
        theta += learning_rate + cost_function_gradient(x, y, theta)
        costs.append(cost_function(x, y, theta))

    return theta, costs

r_theta, costs, thetas = gradient_descent(X, y, theta_0, linear_cost, linear_cost_gradient)

for test_theta in thetas:
    plt.scatter(X[:, 1], y)
    plt.plot(X[:, 1], X @ test_theta, color='g')
    plt.show()