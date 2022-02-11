# Description
# Given a digit string excluded 0 and 1, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.

# 1	2
# ABC	3
# DEF
# 4
# GHI	5
# JKL	6
# MNO
# 7
# PQRS	8
# TUV	9
# WXYZ
# Wechat reply the 【425】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Although the answer above is in lexicographical order, your answer could be in any order you want.

# Example
# Example 1:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# Explanation:
# '2' could be 'a', 'b' or 'c'
# '3' could be 'd', 'e' or 'f'
# Example 2:

# Input: "5"
# Output: ["j", "k", "l"]

LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
        combinations = []

        self.dfs(digits, 0, [], combinations)

        return combinations

    def dfs(self, digits, index, combination, combinations):
        if index == len(digits):
            combinations.append(''.join(combination))
            return

        for letter in LETTERS[digits[index]]:
            combination.append(letter)
            self.dfs(digits, index + 1, combination, combinations)
            combination.pop()


