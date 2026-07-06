# https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=stack

class Solution:
    def isValid(self, s: str) -> bool:
        par = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                par.append(i)
            else:
                if len(par) == 0:
                    return False
                else:
                    if (par[-1] == "(" and i == ")") or (par[-1] == "[" and i == "]") or (par[-1] == "{" and i == "}"):
                        del par[-1]
                    else:
                        return False
        return True if len(par) == 0 else False
        
solve = Solution()
for _ in range(int(input())):
    s = input()
    print(solve.isValid(s))