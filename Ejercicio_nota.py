notaIn = int(input("Introduzca nota:"))
if notaIn < 5:
    calificacion = "Suspenso"
else:
    calificacion = "Aprobado"
print(calificacion)

edad = int(input("Introduce edad: "))
if edad < 18:
    print("No puedes pasar")
elif edad > 18 and edad < 100:
    print("Adelante")
else:
    print("edad incorrecta")
