from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)  # Handle cases where k > len(nums)
        nums[:] = nums[-k:] + nums[:-k]