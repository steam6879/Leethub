# using Slicing
```python3
​class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
```

# using reverse()
```python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
```
