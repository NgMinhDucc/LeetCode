# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rows = rowIndex + 1
        pascal = [[0] * i for i in range(1, rows + 1)]
        pascal[0] = [1]
        for i in range(1, rows):
            for j in range(i):
                pascal[i][j] += pascal[i - 1][j]
            for j in range(i, 0, -1):
                pascal[i][j] += pascal[i - 1][j - 1]
        return pascal[rowIndex]

solve = Solution()
n = int(input())
print(solve.getRow(n))
