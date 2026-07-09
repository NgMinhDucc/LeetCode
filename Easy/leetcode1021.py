# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        ans = ""
        for i in s:
            if not st:
                st.append(i)
            else:
                if i == ")" and st[-1] == "(":
                    st.pop()
                elif i == "(":
                    st.append(i)
                if st:
                    ans += i
        return ans
        
solve = Solution()
for _ in range(int(input())):
    s = input()
    print(solve.removeOuterParentheses(s))