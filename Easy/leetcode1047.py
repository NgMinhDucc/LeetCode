# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) > 0 and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
    
solve = Solution()
for _ in range(int(input())):
    s = input()
    print(solve.removeDuplicates(s))