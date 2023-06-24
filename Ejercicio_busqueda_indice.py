letras = list('abcdefghijklmnopqrstuvwxyz')
vocales = list('aeiou')
for i, letras in enumerate(letras):
    if letras in vocales:
        print('{} está en la posición {}'.format(letras, i))
