# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:     #BFS
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = deque([root])

        while que:
            node = que.popleft()

            if node:
                node.left, node.right = node.right, node.left
                que.append(node.left)
                que.append(node.right)

        return root
