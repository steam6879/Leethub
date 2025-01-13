from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        que = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    que.append((i, j))

        visited = set()
        visited.update(que)
        count = 0

        while que:
            for _ in range(len(que)):
                i, j = que.popleft()

                for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if (0 <= x < rows and
                        0 <= y < cols and
                        (x, y) not in visited):
                        que.append((x, y))
                        visited.add((x, y))

                if mat[i][j] != 0:
                    mat[i][j] += count - 1

            count += 1

        return mat