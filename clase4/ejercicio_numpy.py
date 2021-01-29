import numpy as np

vector = np.arange(5)
matriz = np.arange(15).reshape(3,5)

def dotproduct(x, thetas):
    return x.dot(thetas)

print(dotproduct(matriz,vector))

x = np.array([
    [1, 2],
    [3, 4]
])

x = np.hstack((np.ones(2).reshape(2,1),x))

thetas = np.array([[5], [6], [7]])
print(x@thetas)
