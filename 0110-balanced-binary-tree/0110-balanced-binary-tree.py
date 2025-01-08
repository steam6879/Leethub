class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(node):
            if not node:
                return 0
            
            return 1 + max(depth(node.left), depth(node.right))

        left_depth = depth(root.left)
        right_depth = depth(root.right)

        if abs(left_depth - right_depth) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)