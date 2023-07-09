from collections import namedtuple

# Define una tuple llamada CrateData con los campos 'houses' y 'crates'
CrateData = namedtuple('CrateData', ['houses', 'crates'])

# Averigua la casa o casas que mas reciclan.


def max_recycling(crates):
    """
    Devuelve el índice con el valor más grande en la lista y el número de cajas para esa casa.
    Lanza un ValueError si la lista está vacía.
    """
    if crates is None or len(crates) == 0:
        raise ValueError('Se requiere una lista con al menos un elemento')

    max_houses = []  # Almacena el índice de las casas con la cantidad máxima de reciclaje
    max_crates = crates[0]  # Almacena el número máximo de cajas

    for crate in crates:
        if crate > max_crates:
            max_crates = crate

    for house, crate_count in enumerate(crates):
        if crate_count == max_crates:
            max_houses.append(house)

    return CrateData(max_houses, max_crates)

# Averigua la casa o casas que menos reciclan.


def min_recycling(crates):
    """
    Devuelve el valor más pequeño en la lista y una lista de números de casa (índices de lista) con ese valor.
    Lanza un ValueError si la lista es None o está vacía.
    """
    if crates is None or len(crates) == 0:
        raise ValueError('Se requiere una lista con al menos un elemento')

    min_houses = []  # Almacena el índice de las casas con la cantidad mínima de reciclaje
    min_crates = crates[0]  # Almacena el número mínimo de cajas

    for crate in crates:
        if crate < min_crates:
            min_crates = crate

    for house, crate_count in enumerate(crates):
        if crate_count == min_crates:
            min_houses.append(house)

    return CrateData(min_houses, min_crates)

# Calcula el número de cajas.


def total_crates(crates):
    """Devuelve la suma de todos los valores en la lista de cajas"""
    total = 0

    for crate in crates:
        total += crate

    return total


def get_crate_quantities(houses):
    """Pregunta al usuario por el número de cajas para cada casa"""
    crates = []

    for house in range(houses):
        crates.append(positive_int_input(
            f'Ingrese el número de cajas para la casa {house}'))

    return crates


def positive_int_input(question):
    """Valida que el usuario ingrese un entero positivo"""
    while True:
        try:
            integer = int(input(question + ' '))

            if integer >= 0:
                return integer
            else:
                print('Ingrese un entero positivo.')

        except ValueError:
            print('Ingrese un entero positivo.')


def main():
    print('Programa del camión de reciclaje')
    houses = positive_int_input('¿Cuántas casas hay?')
    crates = get_crate_quantities(houses)
    maximums = max_recycling(crates)
    minimums = min_recycling(crates)
    total = total_crates(crates)
    print('El número total de cajas colocadas en la calle es {}'.format(total))
    print('El número máximo de cajas de cualquier casa es {}'.format(maximums.crates))
    print('La(s) casa(s) con la mayor cantidad de reciclaje es {}'.format(
        maximums.houses))
    print('El número mínimo de cajas de cualquier casa es {}'.format(minimums.crates))
    print('La(s) casa(s) con la menor cantidad de reciclaje es {}'.format(
        minimums.houses))


if __name__ == '__main__':
    main()
