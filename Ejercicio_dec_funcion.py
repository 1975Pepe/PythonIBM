def suma(a, b):  # Definimos la función "suma". Tiene 2 parámetros.
    return a+b


suma(2, 3)  # Llamada a la función. Hay que pasarle dos parámetros. Resultado: 5

x = suma(2,3) #si quisieramos sacar por pantalla el resultado, creamos la variable e imprimimos esta.
print (x)

def en_pantalla(frase1, frase2):
    # "return" no es obligatorio
    print(frase1, frase2)


en_pantalla('Me gusta', 'Python')
# Resultado: Me gusta Python


# Funciones anidadas
def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print(x) # Llamamos a f2 desde f1
    f2(b) # Pasamos a b el valor 100, la función imprime x y al llamar a la función, le pasamos b, que tiene el valor 100 y lo imprime.
f1('Python') # Llamamos a f1

def f(n):
    return(n)
f=("Hola")
print (f)