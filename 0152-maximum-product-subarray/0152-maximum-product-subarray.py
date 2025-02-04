from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        
        max_product = nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            max_product = max(max_product, dp_max[i])

        return max_product
