# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if dic.get(s[i]) == None:
                dic[s[i]] = [i]
            else:
                dic[s[i]].append(i)
        
        for key in dic:
            if len(dic[key]) > 1:
                continue
            else:
                return dic[key][0]
        return -1
    
solve = Solution()
for _ in range(int(input())):
    s = input()
    print(solve.firstUniqChar(s))