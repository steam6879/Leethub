# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = 1 + self.minDepth(root.left)
        rightDepth = 1 + self.minDepth(root.right)

        if leftDepth == 1: return rightDepth
        elif rightDepth == 1: return leftDepth
        
        return min(leftDepth, rightDepth)