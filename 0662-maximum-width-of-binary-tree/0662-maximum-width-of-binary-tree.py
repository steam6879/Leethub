from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        que = deque([(root, 0)])
        max_width = 0

        while que:
            start = que[0][1]

            for _ in range(len(que)):
                node, idx = que.popleft()

                if node.left:
                    que.append((node.left, 2 * idx))
                
                if node.right:
                    que.append((node.right, 2 * idx + 1))

                max_width = max(max_width, idx - start + 1)

        return max_width