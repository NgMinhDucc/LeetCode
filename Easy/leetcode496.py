# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st = []
        mapping = {val: i for i, val in enumerate(nums1)} # reverse the order (key: value -> value: key)
        ans = [-1] * len(nums1)
        for i in nums2:
            while st and i > st[-1]:
                ans[mapping[st.pop()]] = i
            if i in nums1:
                st.append(i)
        return ans
    
solve = Solution()
for _ in range(int(input())):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(solve.nextGreaterElement(arr1, arr2))