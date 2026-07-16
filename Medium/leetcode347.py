# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}
        for i in nums:
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i] += 1
                
        res = sorted(dic, key=lambda x: -dic[x])
        return res[:k]
        
solve = Solution()
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve.topKFrequent(arr, k))