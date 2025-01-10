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

        def dfs(node, path):
            if not node:
                return None

            current_path = path + [node.val]

            if not node.left and not node.right:
                if sum(current_path) == targetSum:
                    self.ans.append(current_path)
                    return None

            dfs(node.left, current_path)
            dfs(node.right, current_path)

        dfs(root, [])
        return self.ans
