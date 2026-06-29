# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = len(a) - 1, len(b) - 1
        carry, summ = 0, 0
        res = ""
        while x >= 0 or y >= 0:
            summ = carry
            if x >= 0:
                summ += int(a[x])
                x -= 1
            if y >= 0:
                summ += int(b[y])
                y -= 1
            if summ > 1:
                if summ % 2 == 0:
                    summ = 0
                    carry = 1
                else:
                    summ = 1
                    carry = 1
            else:
                carry = 0
            res += str(summ % 10)
        if carry == 1:
            return "1" + res[::-1]
        return res[::-1]
            
        
solve = Solution()
for i in range(int(input())):
    a, b = input().split()
    print(solve.addBinary(a, b))