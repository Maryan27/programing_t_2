import unittest
from src.code_pumpkin import generate_matrix
from src.code_pumpkin import calculate_seeds_to_plant


class TestPumpkinRobot(unittest.TestCase):
    def test_pumpkin_robot(self):
        cov = 5
        rov = 5
        pumpkin_counts = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected_seeds = [
            1, 2, 3, 4, 5,
            10, 9, 8, 7, 6,
            11, 12, 13, 14, 15,
            20, 19, 18, 17, 16,
            21, 22, 23, 24, 25
        ]
        self.assertEqual(calculate_seeds_to_plant(cov, rov, pumpkin_counts), expected_seeds)
        
    def test_pumpkin_robot1(self):    
        cov = 2
        rov = 4
        pumpkin_counts = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected_seeds = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(calculate_seeds_to_plant(cov, rov, pumpkin_counts), expected_seeds)

    def test_pumpkin_robot2(self):
        cov = 3
        rov = 3
        pumpkin_counts = [
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
        ]
        expected_seeds = [1, 2, 3, 6, 5, 4, 7, 8, 9]  
        self.assertEqual(calculate_seeds_to_plant(cov, rov, pumpkin_counts), expected_seeds)

    
if __name__ == '__main__':
    unittest.main()
