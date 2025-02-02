from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = None

        def dfs(node):
            if not node or self.ans:
                return None
            
            dfs(node.left)

            self.count += 1
            if self.count == k:
                self.ans = node.val
                return None
            
            dfs(node.right)

        dfs(root)

        return self.ans
