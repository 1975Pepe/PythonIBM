def indexador(objeto, indice):
    return objeto[indice]


try:
    print(indexador('Python', 3)) # Si ponemos una posición que no existe, se captura el error en el try-catch.
except IndexError:  # Captura Indexerror
    print('Has puesto un índice muy grande.')
print('Hemos salido del try-catch')
