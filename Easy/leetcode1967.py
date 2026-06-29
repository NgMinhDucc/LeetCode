# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        cnt = 0
        for pat in patterns:
            if pat in word:
                cnt += 1
        return cnt
    
solve = Solution()
for _ in range(int(input())):
    patterns = input().split()
    word = input()
    print(solve.numOfStrings(patterns, word))