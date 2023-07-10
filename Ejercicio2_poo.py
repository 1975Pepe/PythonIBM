'''En esta sección, se define la clase Cliente que representa a un cliente.
Tiene un constructor (__init__) que recibe tres parámetros: dni, nombre y apellidos.
Estos parámetros se utilizan para inicializar los atributos de la clase.
El método __str__ se utiliza para representar la clase como una cadena de caracteres.
'''

# Creo una estructura para los clientes


class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{}{}'.format(self.nombre, self.apellidos)


'''
En esta sección, se define la clase Empresa que representa a una empresa.
Tiene un constructor (__init__) que recibe un parámetro opcional clientes, que se utiliza para inicializar la lista de clientes de la empresa.
La clase también tiene dos métodos: mostrar_cliente y borrar_cliente.

El método mostrar_cliente recibe un parámetro opcional dni y recorre la lista de clientes de la empresa para buscar un cliente con el mismo DNI.
Si se encuentra el cliente, se imprime su representación como cadena (__str__). Si no se encuentra, se imprime "Cliente no encontrado".

El método borrar_cliente también recibe un parámetro opcional dni y recorre la lista de clientes de la empresa.
Si se encuentra un cliente con el mismo DNI, se elimina de la lista y se imprime un mensaje indicando que el cliente ha sido borrado.
Si no se encuentra, se imprime "Cliente no encontrado".
'''
# Y otra para las empresas


class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i, c in enumerate(self.clientes):
            if c.dni == dni:
                del (self.clientes[i])
                print(str(c), "> BORRADO")
                return
        print("Cliente no encontrado")


'''
En esta sección, se crean dos instancias de la clase Cliente: hector y juan. 
Se pasa la información relevante de cada cliente como argumentos al constructor.

Luego, se crea una instancia de la clase Empresa llamada empresa, y se le pasan los clientes iniciales como argumento al constructor.

A continuación, se imprime la lista de clientes utilizando print(empresa.clientes). 
Luego, se llama al método mostrar_cliente dos veces para mostrar un cliente por su DNI. 
Después, se llama al método borrar_cliente dos veces para borrar un cliente por su DNI.

Finalmente, se imprime nuevamente la lista de clientes para mostrar los cambios.
'''

# Ahora utilizaré ambas estructuras
# Creo un par de clientes
hector = Cliente(nombre="Hector ", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente(nombre="Juan ", apellidos="Gonzalez Marquez", dni="22222222B")

# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])
# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)
print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("22222222B")
print("\n==BORRAR CLIENTES POR DNI==")
# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")
# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)
