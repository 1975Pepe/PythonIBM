class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: Te llamas {self.nombre} y tienes {self.edad} años"


persona = Persona("Pepe", 30)
print(persona)  # Salida: Persona: Juan, 30 años
