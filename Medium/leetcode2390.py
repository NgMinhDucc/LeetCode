# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            # since the input is guaranteed to always be valid, we don't need to check if stack if empty or not
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
    
solve = Solution()
for _ in range(int(input())):
    s = input()
    print(solve.removeStars(s))