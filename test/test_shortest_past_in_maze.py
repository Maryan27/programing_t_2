import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
import unittest
from shortest_path_in_the_maze import shortest_path_in_maze

class TestShortestPathInMaze(unittest.TestCase):
    def test_shortest_path_found(self):
        matrix = [
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1]
        ]
        start = (0, 0)
        finish = (2, 2)
        result = shortest_path_in_maze(matrix, start, finish)
        self.assertEqual(result, 4)

    def test_wrong_destation(self):
        matrix = [
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1]
        ]
        start = (0, 0)
        finish = (3, 3)  
        result = shortest_path_in_maze(matrix, start, finish)
        self.assertIsNone(result)
    
    def test_no_path(self):
        matrix = [
            [1, 1, 1],
            [0, 0, 0],
            [1, 1, 1]
        ]
        start = (0, 0)
        finish = (2, 2)
        self.assertIsNone(shortest_path_in_maze(matrix, start, finish))


if __name__ == '__main__':
    unittest.main()
