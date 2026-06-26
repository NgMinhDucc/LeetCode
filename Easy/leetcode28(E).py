class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
solve = Solution()
for _ in range(int(input())):
    haystack = input()
    needle = input()
    print(solve.strStr(haystack, needle))