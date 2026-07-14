# https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        check = []
        for i in s:
            if i not in check:
                check.append(i)
            else:
                return i
            
solve = Solution()
for _ in range(int(input())):
    s = input()
    print(solve.repeatedCharacter(s))