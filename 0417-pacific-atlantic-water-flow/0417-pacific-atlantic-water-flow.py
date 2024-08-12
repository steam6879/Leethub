from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def bfs(starts):
            que = deque(starts)
            visited = set(starts)
            while que:
                i, j = que.popleft()
                for x, y in [(i, j+1), (i, j-1), (i-1, j), (i+1, j)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[x][y] >= heights[i][j]:
                        que.append((x, y))
                        visited.add((x, y))
            return visited

        pacific = [(i, 0) for i in range(1, m)] + [(0, j) for j in range(n)]
        atlantic = [(i, n-1) for i in range(m-1)] + [(m-1, j) for j in range(n)]

        pacific_reachable = bfs(pacific)
        atlantic_reachable = bfs(atlantic)

        return list(pacific_reachable & atlantic_reachable)
