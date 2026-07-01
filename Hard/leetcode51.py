class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        chessboard = [["."] * n for _ in range(n)]
        col, pri, sec = [False] * n, [False] * (2 * n), [False] * (2 * n)
        
        def n_queens(i):
            for j in range(n):
                if not col[j] and not pri[i - j + n] and not sec[i + j]:
                    # record the queen's position
                    chessboard[i][j] = "Q"
                    col[j] = pri[i - j + n] = sec[i + j] = True
                    if i == n - 1:
                        res.append(["".join(row) for row in chessboard])
                    else:
                        # moving to the next row
                        n_queens(i + 1)
                    # backtracking: remove the previous queen's position
                    chessboard[i][j] = "."
                    col[j] = pri[i - j + n] = sec[i + j] = False
        n_queens(0)
        return res  
    
solve = Solution()
for i in range(int(input())):
    n = int(input())
    print(solve.solveNQueens(n))