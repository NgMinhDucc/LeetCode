# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = [[0] * i for i in range(1, numRows + 1)]
        pascal[0] = [1]
        for i in range(1, numRows):
            for j in range(i):
                pascal[i][j] += pascal[i - 1][j]
            for j in range(i, 0, -1):
                pascal[i][j] += pascal[i - 1][j - 1]
        return pascal

solve = Solution()
n = int(input())
print(solve.generate(n))
