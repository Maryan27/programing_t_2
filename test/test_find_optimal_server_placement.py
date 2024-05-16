import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
import unittest
from find_optimal_server_placement import find_optimal_server_placement, dijkstra

class TestFindOptimalServer(unittest.TestCase):
    def test_find_optimal_server_placement(self):
        graph = {
            1: [(3, 10)],
            2: [(3, 40), (4, 100)],
            3: [(2, 40), (4, 80)],
            4: [(2, 100), (3, 80), (5, 50)],
            5: [(4, 50)]
        }
        clients = {1, 2}
        optimal_server, min_max_delay = find_optimal_server_placement(graph, clients)
        self.assertEqual(optimal_server, 3)
        self.assertEqual(min_max_delay, 40)

    def test_all_clients_connected(self):
        graph = {
            1: [(3, 10)],
            2: [(3, 40), (4, 100)],
            3: [(2, 40), (4, 80)],
            4: [(2, 100), (3, 80), (5, 50)],
            5: [(4, 50)]
        }
        clients = {1, 2, 3, 4, 5}  
        optimal_server, min_max_delay = find_optimal_server_placement(graph, clients)
        self.assertIsNone(optimal_server)  
        self.assertEqual(min_max_delay, float('inf')) 

    def test_duplicate(self):
        graph = {
            1: [(3, 10)],
            2: [(3, 40), (4, 100)],
            3: [(2, 40), (4, 80), (4, 50)],  
            4: [(2, 100), (3, 80), (5, 50)],
            5: [(4, 50)]
        }
        clients = {1, 2}
        optimal_server, min_max_delay = find_optimal_server_placement(graph, clients)
        self.assertEqual(optimal_server, 3)  
        self.assertEqual(min_max_delay, 40)  
    

if __name__ == '__main__':
    unittest.main()

