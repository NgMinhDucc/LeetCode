# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for ops in operations:
            try:
                int(ops)
                record.append(int(ops))
            except ValueError:
                if ops == "C":
                    del record[-1]
                elif ops == "D":
                    record.append(record[-1] * 2)
                elif ops == "+":
                    record.append(record[-1] + record[-2])
        return sum(record)

solve = Solution()
for _ in range(int(input())):
    arr = input().split()
    print(solve.calPoints(arr))