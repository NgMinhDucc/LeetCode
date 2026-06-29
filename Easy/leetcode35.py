# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
solve = Solution()
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    target = int(input())
    print(solve.searchInsert(arr, target))