import numpy as np

#Problema 1
M = np.array([
    [1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1],
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
A = np.arange(0,24,1).reshape(4,6)
print(A)

def rota90(matriz):
    return np.transpose(np.fliplr(matriz))
print(rota90(A))

def rota180(matriz):
    return np.flip(np.transpose(rota90(matriz)),0)
print(rota180(A))

def rota270(matriz):
    return np.flip(np.transpose(rota180(matriz)),0)
print(rota270(A))


def rota90_otro_lado(matriz):
    return np.fliplr(np.transpose(matriz))
print(rota90_otro_lado(A))

def rota180_otro_lado(matriz):
    return np.transpose(np.fliplr(np.transpose(matriz)))
print(rota180_otro_lado(A))

def rota270_otro_lado(matriz):
    return np.fliplr(np.transpose(np.transpose(np.fliplr(np.transpose(matriz)))))
print(rota270_otro_lado(A))

#Problema 4
#x, a, b, y, z, c, t, d
t = np.array([
    [2, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [-1, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, -1, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, -1, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, -1, 2]
])
z = np.array([[4],[3],[3],[3],[2],[1],[6],[4],[2],[-3],[-1],[4]])

resultado = np.linalg.lstsq(t, z)
print(resultado)
resultado_correcto = np.allclose(np.dot(t, z), resultado)
print(resultado_correcto)