# Creación de la clase Coche
class Coche():
    # Declaración del constructor de la clase Coche
    def __init__(self):
        self.largo = 250
        self.ancho = 120
        self.ruedas = 4
        self.peso = 900
        self.color = "rojo"
        self.is_enMarcha = False
    # Declaración de métodos

    def arrancar(self):  # self hace referencia a la instancia de clase.
        self.is_enMarcha = True  # Es como si pusiésemos miCoche.is_enMarcha = True

    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"


    # Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
coche_1 = Coche()
# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
coche_1.ruedas = 7
print("El largo del coche es de", coche_1.largo, "cm.")
coche_1.arrancar()
print(coche_1.estado())
# Acceso a un método de la clase Coche. Nomenclatura del punto.
coche_1.arrancar()
print("En qué estado está el coche?", coche_1.estado())


# Destructores

class Book:
    # Clase para trabajar con libros
    def __init__(self, title, author="", electronic=False):
        self.title = title
        self.author = author
        self.is_electronic = electronic

    def __del__(self):
        print("Acabas de llamar al método destructor. El objeto acaba de ser eliminado")


book = Book("Lazarillo de Tormes")
print(book.title)  # Imprimir el título del libro

# No puedes eliminar directamente el atributo title del objeto book
# Si intentas acceder a book.title después de eliminarlo, obtendrás un error
try:
    del book.title  # Eliminar el atributo title del objeto book
    print(book.title)  # Generará un AttributeError
except AttributeError:
    print("El libro fue eliminado")  # Mensaje personalizado en caso de error.
