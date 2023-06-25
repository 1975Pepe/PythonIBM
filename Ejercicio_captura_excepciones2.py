def indexador(objeto, indice):
    return objeto[indice]


try:
    print(indexador('Python', 'P'))
except IndexError:  # Captura IndexError
    print('Error de índice.')
except TypeError:  # Captura TypeError
    print('El índice tiene que ser un número.')
print('Hemos salido del try-catch')

try:
    print(indexador('Python', 0))
except IndexError:  # Captura IndexError
    print('Error de índice.')
except TypeError:  # Captura TypeError
    print('El índice tiene que ser un número.')
print('Ahora si funciona el código.')
