# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices

solve = Solution()
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(solve.finalPrices(arr))