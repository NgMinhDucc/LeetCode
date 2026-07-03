# https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[len(nums) - 1]
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums) - 1):
                newNums.append((nums[i] + nums[i + 1]) % 10)
            nums = newNums
        return nums[0]
    
solve = Solution()
for i in range(int(input())):
    arr = list(map(int, input().split()))
    print(solve.triangularSum(arr))