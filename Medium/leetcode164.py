# https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums = sorted(nums)
        max_dif = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > max_dif:
                max_dif = nums[i] - nums[i - 1]
        return max_dif
    
solve = Solution()
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(solve.maximumGap(arr))