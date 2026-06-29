class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dic = {}
        for i in nums:
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i] += 1
        for key in dic:
            if dic[key] == 1:
                return key
        
solve = Solution()
for i in range(int(input())):
    nums = list(map(int, input().split()))
    print(solve.singleNumber(nums))