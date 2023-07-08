def decimal(binary_str):
    """ Convierte cadenas binarias a sus equivalentes decimales.
    Lanzar ValueError si binary_str contiene caracteres distintos de 0 y 1"""

    # Verifica si la cadena binaria contiene caracteres distintos de 0 y 1
    remove_0_and_1 = binary_str.replace('0', '').replace('1', '')
    if len(remove_0_and_1) > 0:
        raise ValueError(
            'La cadena binaria de entrada solo puede contener 0 y 1')

    place = 1  # Posición
    dec = 0  # El valor decimal

    # Bucle desde el final de la cadena hasta el principio
    for bit in binary_str[::-1]:
        # Si el dígito es un 1, agregue el valor posicional. Si es 0, ignorar.
        if bit == '1':
            dec += place
        place *= 2  # Multiplique la posición por 2 para el siguiente valor de posición

    # Imprimir el resultado
    print("El valor decimal correspondiente es:", dec)


# Llamada a la función con una cadena binaria
decimal('0101110100')
