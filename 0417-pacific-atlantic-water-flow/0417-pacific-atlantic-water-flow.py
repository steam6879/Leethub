class Solution:    #DFS
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]: 
            return []

        m, n = len(heights), len(heights[0])

        def dfs(i, j, visited):
            visited.add((i, j))
            for di, dj in [(i, j+1), (i, j-1), (i-1, j), (i+1, j)]:
                if 0 <= di < m and 0 <= dj < n and (di, dj) not in visited and heights[di][dj] >= heights[i][j]:
                    dfs(di, dj, visited)

        pacific_reachable = set()
        atlantic_reachable = set()

        # Run DFS from Pacific Ocean borders
        for j in range(n):
            dfs(0, j, pacific_reachable)  # Top row
        for i in range(1, m):
            dfs(i, 0, pacific_reachable)  # Left column

        # Run DFS from Atlantic Ocean borders
        for j in range(n):
            dfs(m-1, j, atlantic_reachable)  # Bottom row
        for i in range(m-1):
            dfs(i, n-1, atlantic_reachable)  # Right column

        return list(pacific_reachable & atlantic_reachable)