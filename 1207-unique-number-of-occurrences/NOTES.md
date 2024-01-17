# Using Counter()
```python3
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        value = Counter(arr).values()
        
        return True if sorted(value) == sorted(set(value)) else False
```
## collections 모듈의 Counter를 사용한다.
Counter를 사용하면 각 원소들이 나오는 빈도수를 세준다.
(ex. a = [1, 1, 2, 3, 3, 3], Counter(a) →→\rightarrow {1: 2, 2: 1, 3: 3})
Counter의 key에는 원소가, value에는 원소의 빈도수들이 저장된다.

python의 set은 중복을 없애준다. (ex. set([1, 1, 2, 3]) →→\rightarrow {1, 2, 3})
따라서 sorted(value) == sorted(set(value))가 성립한다면 빈도수가 중복되지 않으므로 True를 리턴하고, 그렇지 않은 경우에 False를 리턴한다.

* time complexcity: O(n)
