# Description
# Given an expression s contains numbers, letters and brackets. Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.

# Contact me on wechat to get more FLAMG requent Interview questions . (wechat id : jiuzhang15)

# Numbers can only appear in front of “[]”.

# Example
# Example1

# Input: S = abc3[a]
# Output: "abcaaa"
# Example2

# Input: S = 3[2[ad]3[pf]]xyz
# Output: "adadpfpfpfadadpfpfpfadadpfpfpfxyz"
# Challenge
# Can you do it without recursion?

# considering using stack to make it happen

class Solution:

    def expression_expand(self, s):
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)

            temp = []
            while stack and stack[-1] != '[':
                temp.append(stack.pop())
            stack.pop()

            repeats = 0
            base = 1
            while stack and stack[-1].isdidgit():
                repeats += int(stack[-1]) * base
                base *= 10
            stack.append(''.join(reversed(temp)) * repeats)

        return ''.join(stack)