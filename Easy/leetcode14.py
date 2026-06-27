class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lcp = ""
        for i in range(strs[0]):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return lcp
            lcp += strs[0][i]
        return lcp
       
solve = Solution() 
for _ in range(2):
    lis = input().split()
    print(solve.longestCommonPrefix(lis))