
def suma(a, b):
    return a+b


suma(2, 3)
x = suma(2, 3)
print(x)

suma(40, 30)
y = suma(40, 30)
print(y)


def suma(a, b):  # Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b


a, b = 5, 10
print(suma(a, b))
print(a, b)  # a y b no han cambiado fuera de la función


def minimo(l):
    l[0] = 1000  # Modificamos la lista en el interior
    return min(l)


l = [1, 2, 3]
print(l)
# Modifica la lista aquí y al pasar el valor 1000 a la lista, el mínimo pasa a ser 2.
print(minimo(l))
print(l)

# Paso de los valores de los argumentos.


def f(a, b, c):
    print(a, b, c)


f(1, 2, 3)


def f(a, b, c):
    print(a, b, c)


f(c=12, a=10, b=100)


def f(a, b=10, c=30):
    print(a, b, c)


f(1)
f(1, 12)
f(1, 12, 19)
'''
'''
# En la definición de la función se indica que se le pasará un número arbitrario de argumentos
#  que estarán ordenados por posición de izquierda a derecha.


def f(*args):  # Acepta número arbitrario de argumentos
    print(args)


f()  # Si no hay argumentos, args es una tupla vacía
f(1)
f(1, 2)
f(1, 2, 3, 4, 5, 6)

# Con doble asterisco, especificamos que le pasaremos los argumentos por nombre.


def f(**Kargs):  # Acepta número de argumentos por nombre
    print(Kargs)


f()  # Si no hay argumentos, Kargs es un diccionario vacío

f(a=1)
f(a=1, b=2)
f(a=1, c=3, b=2)


def f(a, b, c, d):
    print(a, b, c, d)


argumentos = {'b': 20, 'a': 1, 'c': 300, 'd': 4000}
f(**argumentos)  # Desempaquetando diccionario argumentos con **
argumentos = {'b': 200, 'c': 300, 'd': 400}
f(10, **argumentos)  # Podemos combinar las formas.

#  argumentos sólo puede ser pasado por clave (keyword)


def f(a, *, b, c):  # Define 'b' y 'c' como keyword-only con el *
    print(a, b, c)


f(1, b=10, c=100)
# f(1, 10, 100)  # Error al no pasar argumentos Keyword-only a partir del *.


la = [1, 2, 3, 4, 5]
lb = list('abcde')
lc = list('ABCDE')
zlist = list(zip(la, lb, lc))  # zip soporta cualquier número
# de argumentos posicionales
zlist
a, b, c = zip(*zlist)  # El * en zip desempaqueta lista de tuplas
print(la, lb, lc, sep='\n')
print(la, lb)  # Seperador por defecto es espacio
