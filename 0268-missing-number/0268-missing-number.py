class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expectedSum = (n * (n + 1)) // 2
        sum = 0
        
        for i in nums:
            sum += i
        
        return expectedSum - sum