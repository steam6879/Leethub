# using Slicing
```python3
​class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
```

# using reverse()
```pyhton3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
```
