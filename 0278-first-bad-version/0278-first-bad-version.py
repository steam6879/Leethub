# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # Assuming versions start from 1

        while left < right:
            mid = left + (right - left) // 2  # To avoid integer overflow

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
