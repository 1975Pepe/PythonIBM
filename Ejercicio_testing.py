import unittest
from math import pi


def area(r):
    areaC = pi * (r ** 2)
    return areaC


valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola']

for v in valores:
    areaCalculada = area(v)
    print('Para el valor', v, 'el área es', areaCalculada)


class TestArea(unittest.TestCase):
    def test_area(self):
        print('-----Test valores de resultado conocido-----')
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(3), pi * (3 ** 2))


if __name__ == '__main__':
    unittest.main()


'''
def area(r):

    areaC = pi*(r**2)
    return areaC


valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola']

for v in valores:
    areaCalculada = area(v)
    print('Para el valor', v, 'el área es', areaCalculada)
'''
