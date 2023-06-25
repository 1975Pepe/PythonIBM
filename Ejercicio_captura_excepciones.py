def indexador(objeto, indice):
    return objeto[indice]


try:
    # Si ponemos una posición que no existe, se captura el error en el try-catch.
    print(indexador('Python', 3))
except IndexError:  # Captura Indexerror
    print('Has puesto un índice muy grande.')
print('Hemos salido del try-catch')


def indexador(objeto, indice):
    return objeto[indice]


try:
    indexador('Python', 'h')
except (IndexError, TypeError):  # Captura varios errores
    print('Error.')
print('Hemos salido del try-catch')
try:
    indexador('Python', 'h')
except:  # Captura todos los errores. No recomendado, podríamos estar silenciando excepciones no previstas
    print('Error.')
print('Hemos salido del try-catch')
try:
    # Si ponemos una posición que no existe, se captura el error en el try-catch.
    print(indexador('Python', 0))
except IndexError:  # Captura Indexerror
    print('Has puesto un índice muy grande.')
print('Hemos salido del try-catch')
