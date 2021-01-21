triangle = lambda n : '\n'.join([
    f"{' ' * (n - 1 - i)}{'*' * (2 * i + 1)}"
    for i in range(n,-1,-1)
])


    

print(triangle(4))
print(triangle(5))
print(triangle(6))

#Ejercicio 2

#Ejercicio 3

#Ejercicio 4 (Puntos Extras)