class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countMap = Counter(words)
        heap = [(-counter, word) for word, counter in countMap.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]