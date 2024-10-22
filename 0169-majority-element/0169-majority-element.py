from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counters = Counter(nums)

        for key, value in counters.items():
            if value > len(nums) // 2:
                return key
        
        return None
