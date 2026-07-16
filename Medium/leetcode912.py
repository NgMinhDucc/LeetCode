# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(arr, left, middle, right):
            i, j = left, middle + 1
            tmp = []
            while i <= middle and j <= right:
                if arr[i] <= arr[j]:
                    tmp.append(arr[i])
                    i += 1
                else:
                    tmp.append(arr[j])
                    j += 1
            
            while i <= middle:
                tmp.append(arr[i])
                i += 1
            while j <= right:
                tmp.append(arr[j])
                j += 1
            arr[left:right + 1] = tmp
        
        def merge_sort(arr, left, right):
            if left >= right:
                return
            middle = (left + right) // 2
            
            merge_sort(arr, left, middle)
            merge_sort(arr, middle + 1, right)
            merge(arr, left, middle, right)
            return arr
        
        nums = merge_sort(nums, 0, len(nums) - 1)
        return nums
    
solve = Solution()
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(solve.sortArray(arr))