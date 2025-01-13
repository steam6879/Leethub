class Solution:     # DFS
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def dfs(i, j):
            image[i][j] = color

            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), ((i, j + 1))):
                if (0 <= x < rows and 
                    0 <= y < cols and 
                    image[x][y] == old_color):
                    dfs(x, y)

        # Get dimensions and original color
        rows, cols = len(image), len(image[0])
        old_color = image[sr][sc]

        if old_color != color:
            dfs(sr, sc)

        return image
