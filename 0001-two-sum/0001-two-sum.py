from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List:
        n = len(nums)
        nums_table = {}
        complement = 0

        for i in range(n):
            complement = target - nums[i]

            if complement in nums_table:
                return [nums_table[complement], i]
            else:
                nums_table[nums[i]] = i
        
        return []
