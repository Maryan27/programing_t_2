class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    if root is None:
        return 0
    left_sum = 0
    if root.left:  
        left_sum += root.left.value
        left_sum += branchSums(root.left)  
    if root.right:  
        left_sum += branchSums(root.right.left)
        left_sum += branchSums(root.right)  
    return left_sum
