import unittest
from libreriaComplejos import *
from math import *


class TestComplexMethods(unittest.TestCase):

    def test_add(self):
        c1 = (4, 3)
        c2 = (12, 5)
        self.assertEqual(add(c1, c2), (16, 8))

    def test_dif(self):
        c1 = (4, 5)
        c2 = (12, 5)
        self.assertEqual(dif(c1, c2), (-8, 0))

    def test_modulus(self):
        c = (3, 4)
        self.assertEqual(modulus(c), 5)

    def test_conjugate(self):
        c = (6, 8)
        self.assertEqual(conjugate(c), (6, -8))

    def test_cartesianPolar(self):
        c = (0, 1)
        self.assertEqual(cartesian_polar(c), (1, pi/2))

    def test_polarCartesian(self):
        c = (5, pi/2)
        self.assertEqual(polar_cartesian(c), (0, 5))

    def test_phase(self):
        c = (0, 1)
        self.assertEqual(phase(c), pi/2)

    def test_multiplication(self):
        c1 = (0, 1)
        self.assertEqual(multiplication(c1, c1), (-1, 0))

    def test_division(self):
        c = (0, 1)
        self.assertEqual(division(c, c), (1, 0))

    def test_cToThePowerOf(self):
        c = (0, 1)
        self.assertEqual(cToThePowerOf(c, 3), (0, -1))


if __name__ == '__main__':
    unittest.main()
