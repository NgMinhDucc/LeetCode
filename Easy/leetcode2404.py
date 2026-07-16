# https://leetcode.com/problems/most-frequent-even-element/

from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        even_counter = Counter(i for i in nums if i % 2 == 0) 

        if not even_counter:
            return -1
        
        num, most_freq = -1, - 1
        for k, v in even_counter.items():
            if v > most_freq or (v == most_freq and k < num):
                num, most_freq = k, v
        return num
    
solve = Solution()
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(solve.mostFrequentEven(arr))