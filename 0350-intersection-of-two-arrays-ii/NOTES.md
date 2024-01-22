# array algoritm
```python3
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        interNums = []
        if len(nums1) > len(nums2):
            uniNums, subNums = nums1, nums2
        else:
            uniNums, subNums = nums2, nums1

        for i in subNums:
            if i in uniNums:
                interNums.append(i)
                uniNums.remove(i)

        return interNums
```
​
