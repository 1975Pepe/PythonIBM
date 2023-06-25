def divide(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    else:
        print('El resultado es: ' + str(resultado))
    finally:
        print('Ejecutamos el finally')


divide(12,4)
divide(4, 0)
