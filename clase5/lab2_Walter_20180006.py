import numpy as np

#Problema 1
M = np.array([
    [1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1]
])

M1 = np.array([
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1]
])


#Problema 2

A = np.array([
    [-7, -6, -5],
    [-4, -3, -2]
])

B = np.array([
    [4, 7],
    [10, 13]
])

C = np.array([
    [1., 0.],
    [0., 1.]
])

E = np.array([
    [0., 0., 0.],
    [0., 0., 0.]
])

H = np.array([
    [5., 6., 1., 0., 0., 0., 0.],
    [7., 8., 1., 0., 0.],
    [1., 0., 4., 7., -7., -6., -5.,],
    [0., 1., 10., 13., -4., -3., -2.,]
])


#Problema 3
A = np.arange(0,24).reshape((4,5))





#Problema 4