from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Check if root is null
        if not root:
            return None

        # Check if current node is p or q
        if root == p or root == q:
            return root

        # Search left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search right subtree
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Case 1: Found nodes in both subtrees
        if left and right:
            return root    # Current node is LCA

        # Case 2: Found node only in left subtree
        elif left:
            return left    # LCA is in left subtree

        # Case 3: Found node only in right subtree
        else:
            return right   # LCA is in right subtree