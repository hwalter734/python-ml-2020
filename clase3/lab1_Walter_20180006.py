# Ejercicio 1
triangle = lambda n : '\n'.join([
    f"{' ' * (2 * i + 1)}{'*' * (n - 1 - i)}"
    for i in range(n)
])

    

print(triangle(4))
print(triangle(5))
print(triangle(6))