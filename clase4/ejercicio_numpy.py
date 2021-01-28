import numpy as np

vector = np.arange(5)
matriz = np.arange(15).reshape(3,5)

def dotproduct(x, thetas):
    return x.dot(thetas)

print(dotproduct(matriz,vector))
