# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
    # can be solved with dict as well, but it needs more runtime and space