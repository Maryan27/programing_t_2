import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
import unittest
from find_optimal_server_placement import find_optimal_server_placement, dijkstra


class TestServerPlacement(unittest.TestCase):
    def test_case1(self):
        graph = {
            1: [(2, 6), (3, 10)],
            2: [(1, 6), (3, 40), (4, 100)],
            3: [(1, 10), (2, 40), (4, 80)],
            4: [(2, 100), (3, 80), (5, 50)],
            5: [(4, 50), (6, 20)],
            6: [(5, 20)]
        }
        clients = [1, 2, 3]
        result = find_optimal_server_placement(graph, clients)
        self.assertEqual(result[1], 96)

    def test_case2(self):
        graph = {
            1: [(2, 20), (4, 20)],
            2: [(1, 20), (3, 20), (4, 6), (5, 10)],
            3: [(2, 20), (6, 20)],
            4: [(1, 20), (2, 6), (5, 10), (7, 20)],
            5: [(2, 10), (4, 10), (6, 10), (8, 10)],
            6: [(3, 20), (5, 10), (9, 20)],
            7: [(4, 20), (8, 20)],
            8: [(5, 10), (7, 20), (9, 20)],
            9: [(6, 20), (8, 20)]
        }
        clients = [2, 4, 6]
        result = find_optimal_server_placement(graph, clients)
        self.assertEqual(result[1], 10)

    def test_case3(self):
        graph = {
            1: [(2, 50)],
            2: [(1, 50), (3, 1000000000)],
            3: [(2, 1000000000)]
        }
        clients = [1, 3]
        result = find_optimal_server_placement(graph, clients)
        self.assertEqual(result[1], 1000000000)

if __name__ == "__main__":
    unittest.main()  
