# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last = m + n - 1
        # merge
        while m > 0 and n > 0:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else:
                nums1[last] = nums1[m - 1]
                m -= 1
            last -= 1 # point to the position that is checked last
        # merge the leftover of nums2 into nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            last, n = last - 1, n - 1
        print(nums1)
        
solve = Solution()
for i in range(int(input())):
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    n = int(input())
    solve.merge(arr1, m, arr2, n)