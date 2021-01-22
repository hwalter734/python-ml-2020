triangle = lambda n : '\n'.join([
    f"{'  ' * (i)}{'* ' * ((n + (n-1)) - (2 * i))}"
    for i in range(n)
]); lambda x: '\n'.join([
    f"{' ' * (i + 1)}{'* ' * (h - i - 1)}"
    for i in range(n)
])

print(triangle(4))
print(triangle(5))
print(triangle(6))

#Ejercicio 2


#Ejercicio 3
def diamond(h):
    result = ''
    for i in range(h):
        result += "\n" + f"{' ' * (h - 1 - i)}{'* ' * (i + 1)}"
    for k in range(h):
       result +=  "\n" + f"{' ' * (k + 1)}{'* ' * (h - k - 1)}"
    return result

print(diamond(4))

#Ejercicio 4 (Puntos Extras)