# 처음 시도한 풀이
```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countZero = nums.count(0)
        for i in range(countZero):
            nums.remove(0)
            nums.append(0)
            
        return nums
```
시간이 오래걸린다.​
