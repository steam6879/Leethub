from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        idle_sum = (max_freq - 1) * n

        for count in freq.values():
            idle_sum -= min(max_freq - 1, count)
        
        idle_sum += max_freq - 1

        return len(tasks) + max(0, idle_sum)
