import random
letras = list('abcdefghijklmnopqrstuvwxyz')
l1 = letras[:8]
l2 = letras[8:16:]
l3 = letras[16:]
random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)
for a, b, c in zip(l1, l2, l3):
    print(a + b + c, end=" ")
