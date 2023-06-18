def descomposicion_factores(numero):
    factores = [] #creamos una lista a la que se pueden añadir n valores.
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0: # comprobamos que el resto sea 0.
            factores.append(divisor)
            numero = numero // divisor
        else:
            divisor = divisor + 1

    return factores
numero = 125
resultado = descomposicion_factores(numero)
print(resultado)
