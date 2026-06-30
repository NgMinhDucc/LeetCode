# https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        # applying operations
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        # shift the 0s to the end
        curr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[curr] = nums[curr], nums[i]
                curr += 1
        return nums
    
solve = Solution()
for i in range(int(input())):
    arr = list(map(int, input().split()))
    print(solve.applyOperations(arr))