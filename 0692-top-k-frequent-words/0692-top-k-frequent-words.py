from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))
            
        return [heapq.heappop(heap)[1] for _ in range(k)]
