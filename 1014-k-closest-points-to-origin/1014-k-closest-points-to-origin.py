from typing import List
import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calDistance(x, y):
            return math.sqrt(x ** 2 + y ** 2)

        ans = []
        heap = []

        for point in points:
            [x, y] = point
            heapq.heappush(heap, (calDistance(x, y), point))

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
