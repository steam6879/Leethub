## count(self, value, start, end)
'변수. count(찾는 요소)' 형태로 사용한다. 괄호( ) 안에 찾고자 하는 값을 입력하면 함수를 사용한 변수 안에서 해당 값의 개수를 숫자로 반환한다. 

## remove(self, value)
remove 함수는 값으로 array의 요소를 삭제한다.
사용방법은 array.remove(x) 형태로 사용한다. 괄호( ) 안에 삭제하고자 하는 값을 입력한다. 단, array 안에서 삭제하고자 하는 값이 여러 개가 있다 하더라도 첫 번째 값에 대해서만 삭제한다.
***
# Using two-pointer algorithm
```python3
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
```
