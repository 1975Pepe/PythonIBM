'''
def indexador(objeto, indice):
    return objeto[indice]


try:
    print(indexador('Python', 6))
finally:
    print('Esto se ejecuta incluso cuando salta la excepción')
print('Este print tampoco se ejecuta')
'''

def indexador(objeto, indice):
    return objeto[indice]
try:
    print(indexador('Python', 0))
except IndexError:
    print('Capturamos la excepción')
finally:
    print('Esto se ejecuta incluso cuando salta la excepción')
print('Se ejecutará este print?') 
