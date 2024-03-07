import unittest
from laba2level2 import find_three_numbers

class TestFindThreeNumbers(unittest.TestCase):
    def test_example_case(self):
        array = [1, 2, 3]
        target = 6
        self.assertTrue(find_three_numbers(array, target))

    def test_negative_case(self):
        array = [1, 2, 3, 4, 5]
        target = 20
        self.assertFalse(find_three_numbers(array, target))

if __name__ == '__main__':
    unittest.main()
