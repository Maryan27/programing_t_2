import unittest
from laba3level2 import branchSums
from laba3level2 import BinaryTree


class TestBranchSums(unittest.TestCase):
    def test_left_children(self):
        root = BinaryTree(3)
        root.left = BinaryTree(5)
        root.left.left = BinaryTree(7)
        root.right = BinaryTree(10)
        self.assertEqual(branchSums(root), 5 + 7)

    def test_single_root(self):
        root = BinaryTree(5)
        self.assertEqual(branchSums(root), 0)

if __name__ == '__main__':
    unittest.main()
