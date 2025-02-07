from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = x * x + y * y
            if len(heap) < K:
                heapq.heappush(heap, (-distance, x, y))

            else:
                heapq.heappushpop(heap, (-distance, x, y))

        return [[x, y] for (_, x, y) in heap]
