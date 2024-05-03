import unittest
from love_Valentine_day import find_three_numbers

class TestFindThreeNumbers(unittest.TestCase):
    def test_negative_case(self):
        array = [1, 32, 3, 4, 5, 89, 57, 23, 39, 90]
        target = 20
        self.assertFalse(find_three_numbers(array, target))
     
     def test_positive_case(self):
        array = [1, 2, 3, 4, 5, 6, 8, 9, 7]
        target = 6
        result = find_three_numbers(array, target)
        self.assertTrue(result)
    
     def test_case(self):
        array = [20, 2, 31, 4, 35, 89, 57, 23, 39, 90]
        target = 15
        self.assertFalse(find_three_numbers(array, target))
         
if __name__ == '__main__':
    unittest.main()