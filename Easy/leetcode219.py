# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if seen.get(nums[i]) != None and abs(seen[nums[i]] - i) <= k:
                return True
            seen[nums[i]] = i
        return False
        
solve = Solution()
for i in range(int(input())):
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve.containsNearbyDuplicate(arr, k))
