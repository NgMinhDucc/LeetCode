# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack) > 0 and stack[-1] != s[i] and stack[-1].lower() == s[i].lower():
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
    
solve = Solution()
for _ in range(int(input())):
    s = input()
    print(solve.makeGood(s))