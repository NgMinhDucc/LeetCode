# https://leetcode.com/problems/clear-digits/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) > 0 and i.isdigit():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
    
solve = Solution()
for _ in range(int(input())):
    s = input()
    print(solve.clearDigits(s))