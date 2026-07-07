# https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for log in logs:
            if len(stack) > 0 and log == "../":
                stack.pop()
            elif log == "./":
                continue
            elif log != "../" and log != "./":
                stack.append(log)
        return len(stack)
        
solve = Solution()
for _ in range(int(input())):
    arr = input().split()
    print(solve.minOperations(arr))