from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = [[False for _ in range(n)] for p in range(m)]
        for i in range(m):
            for j in range(n):
                if board[m][n] == 'o':
                    # BFS or DFS


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)

print(board)



