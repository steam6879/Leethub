# Using sort() function
```python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()  #O(logn)
        for i in range(n):  #O(n)
            if nums[i] != i:
                return i
        else:
            return n
```
* Time Complexity - O(nlogn) > O(n) (using summation solution)
