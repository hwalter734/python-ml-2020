import time
import numpy as np

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
def problem2(n, m):
    if m==0:
        return n
    return problem2(n+1,m-1)
print(problem2(50, 35))
print(problem2(100, 85))

#Ejercicio 3
def diamond(h):
    result = ''
    for i in range(h):
        result += "\n" + f"{' ' * (h - 1 - i)}{'* ' * (i + 1)}"
    for k in range(h):
       result +=  "\n" + f"{' ' * (k + 1)}{'* ' * (h - k - 1)}"
    return result

print(diamond(7))
print(diamond(9))
print(diamond(11))

#Ejercicio 4 (Puntos Extras)
def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
#Tomado de https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
start = time.time()
primes(100000)
end = time.time()
print(f"La función se tardó {end-start} segundos")