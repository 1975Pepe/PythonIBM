G = 'Esta variable es de ámbito Global'


def f1():
    E = 'Esta variable es local a f1. Enclosing a f2'

    def f2():
        L = 'Esta variable es local a f2'
        print(L, E, G, sep='\n')
    f2()


f1()

G = 'Esta variable es de ámbito Global'


def f1():
    E = 'Esta variable es local a f1. Enclosing a f2'

    def f2():
        # L, E y G son locales a f2 porque en éste ámbito también se han declarado.
        L = 'L es local a f2'
        E = 'E también es local a f2'
        G = 'G también es local a f2'
        print(L, E, G, sep='\n')
    f2()


f1()

G = 'Esta variable es de ámbito Global'
print(G)


def f1():
    E = 'Esta variable es local a f1. Enclosing a f2'
    print(E)

    def f2():
        L = 'L es local a f2'
        E = 'E también es local a f2'
        G = 'G también es local a f2'
        print(L, E, G, sep='\n')

        def f3():
            print(E, G, sep='\n')
        f3()
    f2()


f1()
