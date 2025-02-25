from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []

        que = deque([root])
        while que:
            level = []

            for _ in range(len(que)):
                node = que.popleft()
                level.append(node.val)

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)
                
            ans.append(level)

        return ans
