# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, currentSum):
            if not root:    #root가 존재하지 않는 예외상황 처리.
                return False
            
            currentSum += root.val  #누적하여 합.
            if not root.left and not root.right:  # Leaf node
                return currentSum == targetSum  #진위판단.
            
            # Recursive calls for left and right subtrees
            return dfs(root.left, currentSum) or dfs(root.right, currentSum)
        
        return dfs(root, 0) #0부터 누적하여 sumation.