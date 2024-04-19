import unittest
from heap_based_priority_queue import PriorityQueue  

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_insert_and_remove_max(self):
        self.pq.insert('1', 5)
        self.pq.insert('2', 3)
        self.pq.insert('3', 7)
        self.assertEqual(self.pq.remove_max(), '3')  

    def test_negative_case(self):
        self.pq.insert('1', 5)
        self.assertFalse(self.pq.insert('1', 3))
        
    def test_duplicates(self):
        self.pq.insert('1', 5)
        self.pq.insert('1', 3)  
        self.pq.insert('3', 7)
        self.pq.insert('3', 2)  
        self.pq.insert('4', 1)
        self.assertEqual(self.pq.remove_max(), '3')  
        self.assertEqual(self.pq.remove_max(), '1')  

if __name__ == '__main__':
    unittest.main()
