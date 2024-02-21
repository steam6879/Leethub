# DFS reculsive algorithm
```
class Solution:    
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        maxdepth=0
        for child in root.children:
            maxdepth=max(self.maxDepth(child),maxdepth)
        return maxdepth+1

```
