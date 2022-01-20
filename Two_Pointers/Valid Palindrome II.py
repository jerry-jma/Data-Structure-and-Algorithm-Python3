# Description
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Wechat reply question number 891 to get Universal algorithm template . (wechat id : jiuzhang15)

# The string will only contain lowercase characters.
# The maximum length of the string is 50000.
# Example
# Example 1:

# Input: s = "aba"
# Output: true
# Explanation: Originally a palindrome.
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: Delete 'b' or 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
# Explanation: Deleting any letter can not make it a palindrome


class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    # def validPalindrome(self, s):
    #     left, right = 0, len(s) - 1

    #     while left < right:
    #         if s[left] != s[right]:
    #             break
    #         left += 1
    #         right -= 1

    #     return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

    # def isPalindrome(self, s, start, end):
    #     i, j = start, end
    #     while i < j:
    #         if s[i] != s[j]:
    #             return False
    #         i += 1
    #         j -= 1

    #     return True

    def validPalindrome(self, s):
        left, right = self.two_pointers(s, 0, len(s) - 1)
        if left >= right:
            return True

        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

    def isPalindrome(self, s, left, right):
        left, right = self.two_pointers(s, left, right)
        return left >= right

    def two_pointers(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1

        return left, right

















