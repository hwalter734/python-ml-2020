import numpy as np
print(type(np.arange(10, 20 , 2)))

my_array = np.linspace(0, 2, 10)
my_array2 = np.full((3,3), 2)
my_array3 = np.eye(5)
print(type(my_array), my_array, my_array.shape)

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
b = np.eye(3)
print(a.dot(b))
print(a @ b)
