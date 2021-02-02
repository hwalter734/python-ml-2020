import numpy as np

#Problema 1
M = np.array([
    [1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
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

M2 = np.array([
    [1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1]
])

def es_reflexiva(x):
    return np.diagonal(x).sum() == x.shape[0]
print(es_reflexiva(M))
print(es_reflexiva(M1))
print(es_reflexiva(M2))

def es_simetrica(x):
    return (np.transpose(x) == x).all()
print(es_simetrica(M))
print(es_simetrica(M1))
print(es_simetrica(M2))

def es_transitiva(x):
    x2 = x@x
    return (x2 <= x).all()
print(es_transitiva(M))
print(es_transitiva(M1))
print(es_transitiva(M2))



#Problema 2
A = np.arange(5,9).reshape((2,2))
B = np.arange(-7,-1, 1).reshape((2,3))
C = np.arange(4,14,3).reshape((2,2))
D = np.eye(2,2)
E = np.zeros((2,3))
H = np.vstack((np.hstack((A,D,E)), np.hstack((D,C,B))))
print(A)
print(B)
print(C)
print(D)
print(E)
print(H)




#Problema 3
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

def rota90(matriz):
    return matriz
# def rota180(self, matriz):
#     return None
# def rota270(self, matriz):
#     return None
# def rota90_otro_lado(self, matriz):
#     return matriz.transpose()
# def rota180_otro_lado(self, matriz):
#     return matriz.transpose()
# def rota270_otro_lado(self, matriz):
#     return None





#Problema 4