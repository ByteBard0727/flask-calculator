import unittest
from app import add, subtract  # Ensure add and subtract are imported

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_division(self):
        self.assertEqual(8 / 4, 2)  # Test basic division
        self.assertEqual(10 / 2, 5)

    def test_multiplication(self):
        self.assertEqual(10 * 2, 20)  # Test basic multiplication
        self.assertEqual(2 * 3, 6)

if __name__ == '__main__':
    unittest.main()