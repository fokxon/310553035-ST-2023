import unittest
import math
from calculator import Calculator


class ApplicationTest(unittest.TestCase):

    def test_add(self):
        args = [(1, 3), (-4, -5), (3.0, -3.0), (0, 7), (0, 0)]
        for first, second in args:
            self.assertEqual(Calculator.add(first, second), first+second)
        self.assertRaises(TypeError, Calculator.add, 1, 'a')

    def test_divide(self):
        args = [(1, 3), (-4, -5), (3.0, -3.0), (0, 7), (99.99, 3)]
        for first, second in args:
            self.assertEqual(Calculator.divide(first, second), first/second)
        self.assertRaises(ZeroDivisionError, Calculator.divide, 1, 0)

    def test_sqrt(self):
        args = [1, 0, 16, 3.3, 17]
        for arg in args:
            self.assertEqual(Calculator.sqrt(arg), math.sqrt(arg))
        self.assertRaises(ValueError, Calculator.sqrt, -4)

    def test_exp(self):
        args = [1, 0, 16, 3.3, -17]
        for arg in args:
            self.assertEqual(Calculator.exp(arg), math.exp(arg))
        self.assertRaises(TypeError, Calculator.exp, 'a')


if __name__ == '__main__':
    unittest.main()
