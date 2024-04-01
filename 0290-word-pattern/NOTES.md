# better solution
```python3
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split()
        m = {}
        
        if len(pattern) != len(sList):  
            return False
        if len(set(pattern)) != len(set(sList)):  # for the case w = ['dog', 'cat'] and p = 'aa'
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in m:
                m[pattern[i]] = sList[i]
            
            elif m[pattern[i]] != sList[i]:
                return False
            
        return True
```
