data = bytes([0x41, 0x42, 0x43, 0x44])  # Datos en forma de bytes

with open('archivo.bin', 'wb') as f:
    f.write(data)


# Leer un archivo binario y mostrar su contenido como bytes
with open('archivo.bin', 'rb') as f:
    data = f.read()
    for byte in data:
        print(byte)

# Cambiar un byte específico en un bytearray
ba = bytearray(b'Hello')
ba[0] = ord('J')  # Cambiar el primer byte a 'J'
print(ba)  # Salida: bytearray(b'Jello')

ba = bytearray(b'Hello')
print(ba)  # Salida: bytearray(b'Hello')
print(type(ba))  # Salida: <class 'bytearray'>
