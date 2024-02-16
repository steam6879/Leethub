# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Base case: If the current node is None, return 0
        if not root:
            return 0
        
        # Check if the left child is a leaf node (has no left or right children)
        if root.left and not root.left.left and not root.left.right:
            # If it is a left leaf, return its value plus the sum of left leaves in the right subtree
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        # If the left child is not a leaf, recursively calculate the sum for left and right subtrees
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)