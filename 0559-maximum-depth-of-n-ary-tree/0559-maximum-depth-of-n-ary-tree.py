from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        que = deque()
        depth = 1
        que.append((root, depth))

        while que:
            node, depth = que.popleft()
            if node.children:
                for child in node.children:
                    que.append((child, depth + 1))
        
        return depth