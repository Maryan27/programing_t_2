import unittest
from sum_left_node import branchSums
from sum_left_node import BinaryTree


class TestBranchSums(unittest.TestCase):
    def test_left_children(self):
        root = BinaryTree(3)
        root.left = BinaryTree(5)
        root.left.left = BinaryTree(7)
        root.right = BinaryTree(10)
        self.assertEqual(branchSums(root), 12)
    
    def test_right_children(self):
        root = BinaryTree(3)
        root.left = BinaryTree(5)
        root.right = BinaryTree(7)
        root.right.right = BinaryTree(10)
        self.assertEqual(branchSums(root), 5)

    def test_single_root(self):
        root = BinaryTree(5)
        self.assertEqual(branchSums(root), 0)

       
if __name__ == '__main__':
    unittest.main()
