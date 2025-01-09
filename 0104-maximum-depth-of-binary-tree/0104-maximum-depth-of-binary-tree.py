# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:     # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        depth = 0

        if not root:
            return 0

        while que:
            depth += 1

            for _ in range(len(que)):
                curr = que.popleft()
                if curr.left:
                    que.append(curr.left)

                if curr.right:
                    que.append(curr.right)

        return depth
