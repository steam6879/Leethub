class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        # Store starting positions where first letter matches
        starting = set()
        # Track visited cells during DFS
        visited = set()

        def backtrack(i, j, ptr):
            # Base case: found complete word
            if ptr == len(word):
                return True
            
            # Mark current cell as visited
            visited.add((i, j))
            
            # Check all 4 adjacent cells
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (0 <= x < m and 0 <= y < n and 
                    board[x][y] == word[ptr] and 
                    (x, y) not in visited):
                    if backtrack(x, y, ptr + 1):
                        return True
            
            # Backtrack by removing current cell from visited
            visited.remove((i, j))
            return False

        # Find all possible starting positions
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    starting.add((i, j))

        # Try DFS from each starting position
        for i, j in starting:
            visited.clear()  # Clear visited set for each new starting point

            if backtrack(i, j, 1):
                return True
        
        return False
