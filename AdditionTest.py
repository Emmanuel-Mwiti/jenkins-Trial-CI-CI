import unittest
from AddNumbers import add_numbers

class TestAddition(unittest.TestCase):

    def test_addition_positive_numbers(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 8, "Test case 1 (addition) failed")

    def test_addition_negative_numbers(self):
        result = add_numbers(-2, -7)
        self.assertEqual(result, -9, "Test case 2 (addition) failed")

    def test_addition_mixed_numbers(self):
        result = add_numbers(10, -4)
        self.assertEqual(result, 6, "Test case 3 (addition) failed")

    def test_addition_float_numbers(self):
        result = add_numbers(3.5, 1.5)
        self.assertEqual(result, 5.0, "Test case 4 (addition) failed")

if __name__ == "__main":
    unittest.main()
