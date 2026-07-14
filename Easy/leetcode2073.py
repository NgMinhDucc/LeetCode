class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        sec = 0
        n = len(tickets)
        while tickets[k] != 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    sec += 1
                    if tickets[k] == 0:
                        return sec
        
        
solve = Solution()
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve.timeRequiredToBuy(arr, k))