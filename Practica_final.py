# Importamos el módulo random que vamos a utilizar después para utilizar números aleatorios.
import random


def generar_matriz(n):
    # Creamos la matriz y le llenamos con números de 0 a 9.
    matriz = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    return matriz


def calcular_sumas(matriz):
    # Función para calcular la suma de las filas y columnas.
    filas = []
    columnas = []

    for i in range(len(matriz)):
        # Calculamos la suma de las filas.
        suma_fila = sum(matriz[i])
        filas.append(suma_fila)

        # Aquí calculamos la suma de las columnas.
        suma_columna = sum(matriz[j][i] for j in range(len(matriz)))
        columnas.append(suma_columna)

    return filas, columnas


def imprimir_matriz(matriz):
    # Sacamos por consola la matriz.
    for fila in matriz:
        print(fila)


def imprimir_sumas(filas, columnas):
    # Imprimimos la suma de cada fila
    print("Suma de cada fila:")
    for suma_fila in filas:
        print(suma_fila)

    # Imprimimos la suma de cada columna
    print("Suma de cada columna:")
    for suma_columna in columnas:
        print(suma_columna)


# Obtenemos el tamaño de la matriz del usuario y nos aseguramos de que sea un entero positivo.
while True:
    try:
        n = int(input("Dime el tamaño de la matriz (N): "))
        if n <= 0:
            print("Error: Ingresa un valor entero positivo.")
        else:
            break
    except ValueError:
        print("Error: Ingresa un valor entero válido.")

# Generar la matriz con el dato introducido por el usuario.
matriz = generar_matriz(n)

# Imprimimos la matriz generada
print("Matriz generada:")
imprimir_matriz(matriz)

# Calculamos la suma de cada fila y columna
filas, columnas = calcular_sumas(matriz)

# Imprimimos la suma de cada fila y columna
imprimir_sumas(filas, columnas)
