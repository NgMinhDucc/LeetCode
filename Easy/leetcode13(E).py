class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0
        i = 0
        while i < len(s) - 1:
            first, second = s[i], s[i + 1]
            if roman[first] >= roman[second]:
                integer += roman[first]
                i += 1
            else:
                integer += (roman[second] - roman[first])
                i += 2
        while i < len(s):
            integer += roman[s[i]]
            i += 1
        return integer
    
solve = Solution()
for _  in range(3):
    s = input()
    print(solve.romanToInt(s))