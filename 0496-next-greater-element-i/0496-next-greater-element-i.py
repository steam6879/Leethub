from typing import Optional, List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)  # Initialize ans with -1
        
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            for k in range(j + 1, len(nums2)):
                if nums2[k] > nums1[i]:  # Compare with nums1[i], not nums2[j]
                    ans[i] = nums2[k]
                    break
        return ans