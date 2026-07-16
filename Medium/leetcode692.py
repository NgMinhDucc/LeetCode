# https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        dic = {}
        for w in sorted(words):
            if dic.get(w) == None:
                dic[w] = 1
            else:
                dic[w] += 1
        
        res = sorted(dic, key=lambda x: -dic[x])
        return res[:k]

solve = Solution()
for _ in range(int(input())):
    arr = input().split()
    k = int(input())
    print(solve.topKFrequent(arr, k))