# DFS algorithm
```python3
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
```
Although recursion can be difficult to wrap your head around initially, once you understand the concept, it can be used to solve many problems in a very concise and elegant way.

In this solution, the base case is when root == None, which is when the end of a path is reached, so we return 0.

If the root is not None, then we recursively call the maxDepth function twice: once for the left child node and once for the right child node until every branch has been fully explored. Then when going back up the tree, we return 1 + max(left_depth, right_depth), which finds the longest branch of the current node, and adds 1 to include the current node. This propagates all the way up to the root node, where the final maximum depth is returned.

[YOUTUBE] https://www.youtube.com/watch?v=p-eMCRpvbIY
