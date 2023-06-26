miLista = ["Angel", 43, 667767250]
miLista2 = [22, True, "una lista", [1, 2]]
print(type(miLista))
print(miLista[0])

miLista = [22, True]
miLista[0] = 99  # Con esto valdrá [99,true]
print(miLista)

miLista1 = ["Angel", "Maria", "Manolo", "Antonio", "Pepe"]
# Se puede mezclar diferentes elementos. Para un elemento en concreto, se empieza a contar desde la posición cero.
miLista2 = ["Maria", 2, 5.56, True]
print(miLista1[1])
print(miLista2[0:2])

c = "hola mundo"
print(c[0])  # h
print(c[5:])  # mundo
print(c[::3])  # hauo

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Convertir lista en tupla y viceversa.
x = ("apple", "banana", "cherry")
y = list(x)
print(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Recorrer una tupla.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


# Comprobar si existe un elemento.
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Determinar la longitud de una tupla
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

'''
# Agregar elementos, NO SE PUEDEN AGREGRAR NUEVOS ELEMENTOS
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange"  # This will raise an error
print(thistuple)
'''

# Para crear una tupla de un elemento hay que poner una ',' al final
thistuple = ("apple",)
print(type(thistuple))
print(thistuple)

'''
# No se pueden eliminar elementos de una tupla, pero si se puede eliminar una tupla
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists
'''

# Unir tuplas.
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Uso de constructor tuple para crear una tupla. Note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

miTupla = ("Angel", 4, 5.345, True, 4)
tuplaUnitaria = ("Sara",)
print(miTupla[2])
miLista = list(miTupla)
miTupla2 = tuple(miLista)
print("Angel" in miTupla)
# Cuenta las veces que se repite el elemento 4 en la tupla.
print(miTupla.count(4))
print(len(miTupla))
