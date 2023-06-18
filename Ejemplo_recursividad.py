def factorial(x):
    if x > 1:
        return x*factorial(x-1)
    else:
        return 1

factorial(5)
x=factorial(5)
print(x)

def maxmin(lista):
    return max(lista), min(lista) # Devielveuna tupla de 2 elementos
l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(l) # Desempaqueta la tupla en 2 variables
print(minimo, maximo, sep= ' ')
