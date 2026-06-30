# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        curr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[curr] = nums[curr], nums[i]
                curr += 1
        print(nums)
        
solve = Solution()
for i in range(int(input())):
    arr = list(map(int, input().split()))
    solve.moveZeroes(arr)