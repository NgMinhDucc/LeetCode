# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        curr = 0
        k = 1
        for i in range(1, len(nums)):
            if nums[curr] != nums[i]:
                k += 1
                curr += 1
                nums[curr] = nums[i]
        return k

solve = Solution()
for i in range(int(input())):
    arr = list(map(int, input().split()))
    print(solve.removeDuplicates(arr))