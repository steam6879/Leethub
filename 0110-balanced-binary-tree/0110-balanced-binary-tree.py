class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0

            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)

            if abs(left - right) > 1:
                self.ans = False

            return max(left, right)

        self.ans = True
        dfs(root)

        return self.ans