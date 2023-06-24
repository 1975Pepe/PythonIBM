# Pedir un valor.

nombre = input('Dime como te llamas: ')
print("Hola, " + nombre)
print(type(nombre))  # Con esto sabemos de que tipo es la variable nombre.

# Pedir varios valores a la vez.

a, b, c = map(int, input("Introduzca los números: ").split())
print("Los números son: ", end=" ")
print(a, b, c)
