import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
import unittest
from minimum_cable_length import minimum_cable_length

class TestMinimumCableLength(unittest.TestCase):
    def test_minimum_cable_length_connection(self):
        graph = [
            [0, 1, 3, 4],
            [1, 0, 2, 5],
            [3, 2, 0, 6],
            [4, 5, 6, 0]
        ]
        self.assertEqual(minimum_cable_length(graph), 7) 

    def test_minimum_cable_length_indirect_possible_connection(self):
        graph = [
            [0, 10, 20],
            [10, 0, 30],
            [20, 30, 0]
        ]
        self.assertEqual(minimum_cable_length(graph), 30)  

    def test_minimum_cable_length_impossible_connection(self):
        graph = [
            [0, 1, 3, 0],
            [1, 0, 2, 0],
            [3, 2, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(minimum_cable_length(graph), 0)  

if __name__ == '__main__':
    unittest.main()
