# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        curr = len(nums) - 1
        k = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[curr] == val:
                curr -= 1
                k += 1
            elif nums[i] == val:
                nums[i] = nums[curr]
                curr -= 1
                k += 1
        return len(nums) - k
        
solve = Solution()
for i in range(int(input())):
    arr = list(map(int, input().split()))
    val = int(input())
    print(solve.removeElement(arr, val))