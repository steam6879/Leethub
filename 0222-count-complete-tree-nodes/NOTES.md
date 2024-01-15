> This **recursive approach** counts the current node and recursively counts the nodes in the left and right subtrees. This should give you the correct count for any binary tree, not just complete binary trees.​
>
>  by chatGPT

# Wrong Answer
```python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        pl, pr = 1, 1

        if root is None:
            return 0

        while root.left:
            pl += 1
            root = root.left

        while root.right:
            pr += 1
            root = root.right

        if pl == pr:
            return 2**pl - 1

        else:
            return 2**pl - 2
```
this code don't take correct answer
