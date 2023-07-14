import unittest
import random


class Matriz:
    def __init__(self, n):
        """
        Inicializa una nueva instancia de la clase Matriz.

        Args:
            n (int): El tamaño de la matriz cuadrada.
        """
        self.n = n
        self.matriz = self.generar_matriz()

    def generar_matriz(self):
        """
        Genera una matriz cuadrada con números aleatorios entre 0 y 9.

        Returns:
            list: La matriz generada.
        """
        matriz = [[random.randint(0, 9) for _ in range(self.n)]
                  for _ in range(self.n)]
        return matriz

    def calcular_sumas(self):
        """
        Calcula la suma de los elementos de cada fila y columna de la matriz.

        Returns:
            tuple: Una tupla que contiene las listas de las sumas de filas y columnas.
        """
        filas = []
        columnas = []
        for i in range(self.n):
            suma_fila = sum(self.matriz[i])
            filas.append(suma_fila)

            suma_columna = sum(self.matriz[j][i] for j in range(self.n))
            columnas.append(suma_columna)

        return filas, columnas

    def imprimir_matriz(self):
        """
        Imprime la matriz generada en pantalla.
        """
        for fila in self.matriz:
            print(fila)

    def imprimir_sumas(self, filas, columnas):
        """
        Imprime la suma de cada fila y columna en pantalla.

        Args:
            filas (list): La lista de sumas de filas.
            columnas (list): La lista de sumas de columnas.
        """
        print("Suma de cada fila:")
        for suma_fila in filas:
            print(suma_fila)

        print("Suma de cada columna:")
        for suma_columna in columnas:
            print(suma_columna)


class TestMatriz(unittest.TestCase):
    def test_generar_matriz(self):
        # Prueba la generación de una matriz
        matriz = Matriz(3)
        # Verifica el tamaño de la matriz
        self.assertEqual(len(matriz.matriz), 3)
        for fila in matriz.matriz:
            self.assertEqual(len(fila), 3)  # Verifica el tamaño de cada fila

    def test_calcular_sumas(self):
        # Prueba el cálculo de sumas de filas y columnas
        matriz = Matriz(3)
        filas, columnas = matriz.calcular_sumas()
        # Verifica las sumas de las filas
        self.assertEqual(filas, [sum(fila) for fila in matriz.matriz])
        # Verifica las sumas de las columnas
        self.assertEqual(columnas, [sum(columna)
                         for columna in zip(*matriz.matriz)])


if __name__ == '__main__':
    # Obtener el tamaño de la matriz del usuario
    while True:
        try:
            n = int(input("Ingresa el tamaño de la matriz (N): "))
            if n <= 0:
                print("Error: Ingresa un valor entero positivo.")
            else:
                break
        except ValueError:
            print("Error: Ingresa un valor entero válido.")

    # Crear una instancia de la clase Matriz
    matriz = Matriz(n)

    # Imprimir la matriz generada
    print("Matriz generada:")
    matriz.imprimir_matriz()

    # Calcular la suma de cada fila y columna
    filas, columnas = matriz.calcular_sumas()

    # Imprimir la suma de cada fila y columna
    matriz.imprimir_sumas(filas, columnas)

    # Ejecutar las pruebas unitarias
    unittest.main()
