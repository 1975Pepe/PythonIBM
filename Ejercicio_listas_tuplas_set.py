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
