import unittest
from main import add, multiply, substract, divide #assuming these functions are in the main.py file under src folder

class TestArithmeticFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 7), 12)

    def test_multiply(self):
        self.assertEqual(multiply(5, 7), 35)

    def test_substract(self):
        self.assertEqual(substract(10, 5), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()

# (project's directory)$ python -m unittest discover src/