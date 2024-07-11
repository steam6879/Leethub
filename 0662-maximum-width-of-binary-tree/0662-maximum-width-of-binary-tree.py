from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Return 0 for an empty tree or None

        que = deque([(root, 0)])  # Initialize deque with (node, index)
        maxWidth = 0  # Initialize maximum width to 0

        while que:
            _, start = que[0]  # Get the index of the first element in current level

            for _ in range(len(que)):
                node, idx = que.popleft()  # Dequeue the node and its index

                if node.left:
                    que.append((node.left, 2 * idx))  # Add left child with doubled index

                if node.right:
                    que.append((node.right, 2 * idx + 1))  # Add right child with doubled index + 1

                maxWidth = max(maxWidth, idx - start + 1)  # Calculate current level width

        return maxWidth
