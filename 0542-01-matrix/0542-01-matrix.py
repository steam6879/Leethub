from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        que = deque()
        
        # Initialize distances and queue
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    que.append((i, j))
                else:
                    mat[i][j] = float('inf')
        
        # BFS
        while que:
            i, j = que.popleft()
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if (0 <= x < rows and
                    0 <= y < cols and
                    mat[x][y] > mat[i][j] + 1):
                    mat[x][y] = mat[i][j] + 1
                    que.append((x, y))
                    
        return mat