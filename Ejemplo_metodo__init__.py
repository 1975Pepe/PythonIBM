class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona = Persona("Pepe", 30)
print("Te llamas ", persona.nombre, " y tienes ", (persona.edad), " años")


"""
El método `__init__()` es un método especial en Python que se utiliza para 
inicializar un objeto recién creado de una clase. Es conocido como el "constructor" de la clase.

Cuando se crea una instancia de una clase en Python utilizando la sintaxis de `objeto = Clase()`, el método `__init__()`
se ejecuta automáticamente para realizar cualquier inicialización necesaria en el objeto.

En este ejemplo, la clase `Persona` tiene un método `__init__()` que toma dos parámetros, `nombre` y `edad`.
Cuando se crea una instancia de `Persona` y se pasa el nombre y la edad como argumentos, el método `__init__()` se ejecuta automáticamente.
Dentro de este método, se asignan los valores de `nombre` y `edad` a los atributos correspondientes de la instancia(`self.nombre` y `self.edad`).

El método `__init__()` se utiliza comúnmente para realizar cualquier inicialización necesaria en un objeto,
como la asignación de valores iniciales a los atributos. Puede recibir cualquier número de parámetros,
aunque el primer parámetro debe ser `self`, que es una referencia al propio objeto.

Es importante destacar que el método `__init__()` no devuelve ningún valor explícito, ya que su propósito es inicializar el objeto
y no generar una salida en particular.
"""
