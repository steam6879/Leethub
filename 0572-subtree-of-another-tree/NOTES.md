# BSF algoritms
```python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return identical(p.left, q.left) and identical(p.right, q.right)

        que = collections.deque()
        que.append(root)

        while que:
            node = que.popleft()
            if node.val == subRoot.val and identical(node, subRoot):
                return True

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return False
```

# DFS algoritms
```python3
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if identical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def identical(p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return identical(p.left, q.left) and identical(p.right, q.right)
```
