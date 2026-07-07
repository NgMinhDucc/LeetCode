# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        circles, squares = 0, 0
        # count the numbers of students who like circular or square sandwich
        for i in students:
            if i == 0:
                circles += 1
            else:
                squares += 1
        for i in sandwiches:
            if i == 0 and circles == 0: # all of these students like square sandwiches
                return squares
            elif i == 1 and squares == 0: # all of these students like circular sandwiches
                return circles
            elif i == 0:
                circles -= 1
            elif i == 1:
                squares -= 1
        return 0

solve = Solution()
for _ in range(int(input())):
    stu = list(map(int. input().split()))
    san = list(map(int, input().split()))
    print(solve.countStudents(stu, san))