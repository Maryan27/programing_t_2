import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
import unittest
from i_jones_and_the_last_walk import counting_ways_to_pass_the_corridor

class TestCountingWays(unittest.TestCase):
    def test_case1(self):
        columns = 3
        rows = 3
        matrix = [
            ['a', 'a', 'a'],
            ['c', 'a', 'b'],
            ['d', 'e', 'f']
        ]
        expected_result = 3
        result = counting_ways_to_pass_the_corridor(columns, rows, matrix)
        self.assertEqual(result, expected_result)

    def test_case2(self):
        columns = 10
        rows = 1
        matrix = [['a', 'b', 'c', 'd', 'e', 'f', 'a', 'g', 'h', 'i']]
        expected_result = 2
        result = counting_ways_to_pass_the_corridor(columns, rows, matrix)
        self.assertEqual(result, expected_result)

    def test_case3(self):
        columns = 7
        rows = 6
        matrix = [
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a']
        ]
        expected_result = 93312
        result = counting_ways_to_pass_the_corridor(columns, rows, matrix)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
