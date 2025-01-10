from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        self.ans = []

        def dfs(node, currentSum, path):
            if not node:
                return

            currentSum += node.val
            path.append(node.val)

            if not node.left and not node.right and currentSum == targetSum:
                self.ans.append(path[:])

            dfs(node.left, currentSum, path)
            dfs(node.right, currentSum, path)
            path.pop()

        dfs(root, 0, [])
        return self.ans