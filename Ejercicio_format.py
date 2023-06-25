# Declaramos de variables
a = 20
b = 10
# Suma
sum = a+b
# Resta
sub = a-b

# Salida
'''La función format() se utiliza para formatear el texto de salida
y reemplazar los espacios reservados {} con los valores de a y b respectivamente.'''
print('El valor de a es {} y b es {}'.format(a, b))

# En orden, a toma el valor de la posición 0, b de la posición 1 y sum de la posición 2.
print('{2} es la suma de {0} y {1}'.format(a, b, sum))

print('{sub_value} es la resta de {value_a} y {value_b}'.format(
    value_a=a, value_b=b, sub_value=sub))


# Entrada de datos
num = int(input("Introduzca un número: "))
add = num+5
# Salida
# Con %d --> número entero, %f --> flotante, %s --> cadena...
print("La suma es %d" % add)
