class Solution:     # Copilot ver``
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:  # Base case: empty tree
            return None
            
        # Get root value from preorder and find its position in inorder
        root_val = preorder.pop(0)
        root_idx = inorder.index(root_val)
        
        # Create root node
        root = TreeNode(root_val)
        
        # Build left subtree: elements before root in inorder
        root.left = self.buildTree(preorder, inorder[:root_idx])
        
        # Build right subtree: elements after root in inorder
        root.right = self.buildTree(preorder, inorder[root_idx + 1:])
        
        return root