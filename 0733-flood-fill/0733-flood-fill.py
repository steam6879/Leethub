class Solution:     # DFS
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def dfs(i, j):
            image[i][j] = color

            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), ((i, j + 1))):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)

        m, n, old = len(image), len(image[0]), image[sr][sc]
        if old != color:
            dfs(sr, sc)

        return image
