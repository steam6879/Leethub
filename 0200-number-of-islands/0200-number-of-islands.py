class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid: return 0

        visited = set()
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            visited.add((i, j))

            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (0 <= x < m and 0 <= y < n
                    and grid[x][y] == '1' 
                    and (x, y) not in visited):
                    
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    dfs(i,j)

        return count
