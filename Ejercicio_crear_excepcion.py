'''
class miError(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)
raise(miError('Mensaje de error'))
'''

# Ejemplo de uso de la excepción creada.


class miError(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)


def dividir(a, b):
    if b == 0:
        raise miError("No se puede dividir entre cero")
    return a / b


try:
    # Si escribimos dividir(10, 0) salta la excepción. En este caso nos muestra el resultado.
    resultado = dividir(10, 2)
    print("El resultado de la división es:", resultado)
except miError as e:
    print("Se produjo un error personalizado:", e)
