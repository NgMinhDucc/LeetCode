# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        st = []
        maxx = 0
        for i in s:
            if i == "(":
                st.append(i)
            elif i == ")":
                st.pop()
            if len(st) >= maxx:
                maxx = len(st)
        return maxx

solve = Solution()
for _ in range(int(input())):
    s = input()
    print(solve.maxDepth(s))