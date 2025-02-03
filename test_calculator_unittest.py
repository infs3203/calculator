import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a Calculator instance before each test"""
        self.calc = Calculator()

    def test_add(self):
        """Test addition operation"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test subtraction operation"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        """Test multiplication operation"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """Test division operation"""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 2), -3)

    def test_divide_by_zero(self):
        """Test division by zero returns appropriate message"""
        self.assertEqual(self.calc.divide(5, 0), "Cannot divide by zero")

    def test_modulo(self):
        """Test modulo operation"""
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(7, 3), 1)
        self.assertEqual(self.calc.modulo(10, 5), 0)

    def test_power(self):
        """Test power operation"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(3, 2), 9)
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_square_root(self):
        """Test square root operation"""
        self.assertAlmostEqual(self.calc.square_root(4), 2)
        self.assertAlmostEqual(self.calc.square_root(9), 3)
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951, places=10)

if __name__ == '__main__':
    unittest.main() 