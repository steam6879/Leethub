
## zip 함수를 이용
같은 문자만 튜플로 나열한 후 tuple type를 set type로 바꾸어 중복을 제거하고 if len(set(a)) == 1 을 이용하는 아이디어이다.
```python3
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for a in zip(*strs):
            if len(set(a)) == 1: 
                res += a[0]
            else: 
                return res
        return res
```

## sorted함수를 이용
sorted를 하여 사전순으로 나열하면 first와 last가 가장 차이가 많이 나기 때문에 둘만을 비교하는 것으로 간략화 할 수 있다.
```
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]

        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            
            ans+=first[i]
            
        return ans
```


***
### solution 보기 전 만든 코드
```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cnt = 0
        min_strs = min(strs)
        n = len(min(strs))
        m = {}

        for i in range(n):  #hash map
            m[min_strs[i]] = i
        
        for ptr in strs:
            for i in range(n):
                if ptr[i] not in m:
                    return cnt
                
                else:
                    if ptr == str[-1]:
                        cnt += 1
                
        return cnt
```
