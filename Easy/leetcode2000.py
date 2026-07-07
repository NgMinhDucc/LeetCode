# https://leetcode.com/problems/reverse-prefix-of-word/description/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        idx = word.find(ch)
        for i in range(idx + 1):
            stack.append(word[i])
        return "".join(stack[::-1]) + word[idx + 1:]

solve = Solution()
for _ in range(int(input())):
    s = input()
    ch = input()
    print(solve.reversePrefix(s, ch))