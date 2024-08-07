class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i, j, k):
            if k == len(word):
                return True
            
            # Check if out of bounds or cell does not match the word
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            # Save the current cell and mark it as visited
            temp = board[i][j]
            board[i][j] = '#'
            
            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True

            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False