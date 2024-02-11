```python3
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, currentSum):
            if not root:
                return False
            currentSum += root.val
            if not root.left and not root.right:  # Leaf node
                return currentSum == targetSum
            # Recursive calls for left and right subtrees
            return dfs(root.left, currentSum) or dfs(root.right, currentSum)
        
        return dfs(root, 0)

```
* We define a nested dfs function to perform a depth-first search.
* We pass the current sum from the root to the current node to each recursive call.
* At each node, we check if it's a leaf node and if the cumulative sum equals the targetSum.
* If the current node is not a leaf node, we continue recursively checking its left and right children.
* Finally, we return True if we find a path with the targetSum, otherwise False.​

# 2nd Solution
```python3
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        if targetSum - root.val == 0 and not root.left and not root.right:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)

```

# iterative algoritm
```python3
class Solution(object):
    def hasPathSum(self, root, targetSum):
        stack = [(root, targetSum)]
        
        while stack:
            node, sum = stack.pop()
            
            if not node:
                continue
            
            if not node.left and not node.right and node.val == sum:
                return True
            
            stack.append((node.right, sum-node.val))
            stack.append((node.left, sum-node.val))
            
        return False
```
