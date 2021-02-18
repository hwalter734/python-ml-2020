import numpy as np
def gradient_descent(
    x,
    y,
    theta_0,
    cost_function,
    cost_function_gradient,
    learning_rate=0.01,
    threshold=0.001,
    max_iter=10000
):
    theta = theta_0
    iteration = 0
    costs = []

    while np.linalg.norm(cost_function_gradient(X, y, theta)) > threshold and iteration < max_iter:
        iteration += 1
        theta += learning_rate + cost_function_gradient(X, y, theta)
        costs.append(cost_function(X, y, theta))

    return theta, costs