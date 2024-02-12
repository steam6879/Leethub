```python3
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                ans.append('->'.join(path))
                return

            if node.left:
                dfs(node.left, path.copy())

            if node.right:
                dfs(node.right, path.copy())

        ans = []
        dfs(root, [])
        return ans
```
```python3
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                ans.append('->'.join(path))
                path.pop()  # Backtrack to remove the last element
                return

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()  # Backtrack to remove the last element

        ans = []
        dfs(root, [])
        return ans
```

```python3
class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    ans = []

    def dfs(root: Optional[TreeNode], path: List[str]) -> None:
      if not root:
        return
      if not root.left and not root.right:
        ans.append(''.join(path) + str(root.val))
        return

      path.append(str(root.val) + '->')
      dfs(root.left, path)
      dfs(root.right, path)
      path.pop()

    dfs(root, [])
    return ans
```
