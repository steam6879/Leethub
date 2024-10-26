from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and multiply with prefix
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans
