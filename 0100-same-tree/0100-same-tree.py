# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:     # DFS
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True

            elif not p or not q:
                return False

            elif p.val != q.val:
                return False
            
            else:
                return dfs(p.left, q.left) \
                    and dfs(p.right, q.right)

        return dfs(p, q)