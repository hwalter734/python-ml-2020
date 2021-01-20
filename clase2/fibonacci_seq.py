'''
Pure functions:
1. Dependen unicamente de los parametros
2. No tienen random
3. No tienen efectos colaterales

Las funciones puras son memoizables.
'''
cache = {}
def fibo(n):
    if n in cache:
        return cache[n]
    result = 1
    if n < 2:
        return 1
    result = fibo(n-1) + fibo(n-2)
    cache[n] = result
    return result

print(fibo(5))