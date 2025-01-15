from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone = Node(node.val)
        clones = {node: clone}
        que = deque([node])

        while que:
            node = que.popleft()
            for nei in node.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    que.append(nei)

                clones[node].neighbors.append(clones[nei])

        return clone
