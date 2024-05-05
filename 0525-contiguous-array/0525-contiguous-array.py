class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        maxLength = 0
        m = {0: -1}
        count = 0

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in m:
                maxLength = max(maxLength, i - m[count])
            else:
                m[count] = i

        return maxLength