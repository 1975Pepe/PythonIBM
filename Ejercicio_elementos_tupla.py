# Agregar un elemento a una tupla.
T = (2, 3, 4, 5, 6)
print("Tupla inicial")
print(T)
L = list(T)  # Convertimos la tupla en una lista.
L.append(int(input("Introduzca el nuevo elemento: ")))
# L = tuple(T)
T = list(L)  # Pasamos la lista a tupla.
print("Tupla final")
print(T)
