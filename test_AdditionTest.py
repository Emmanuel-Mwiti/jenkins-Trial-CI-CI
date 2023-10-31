import unittest
from AddNumbers import add_numbers

class TestAddition(unittest.TestCase):

    def test_addition_positive_numbers(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 8, "Test case 1 (addition) failed")

if __name__ == "__main":
    unittest.main()
