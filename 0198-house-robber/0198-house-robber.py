class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2, prev, curr = 0, 0, 0
        for num in nums:
            curr = max(prev, prev2 + num)
            prev2 = prev
            prev = curr
        
        return curr