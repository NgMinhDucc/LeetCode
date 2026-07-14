# https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        sec = 0
        n = len(tickets)
        for i in range(n):
            if i <= k: # ahead or at position k
                sec += min(tickets[i], tickets[k])
            else: # behind position k
                sec += min(tickets[i], tickets[k] - 1) # after buying 1 ticket, we only have tikets[k] tickets more to buy
        return sec
        
solve = Solution()
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve.timeRequiredToBuy(arr, k))