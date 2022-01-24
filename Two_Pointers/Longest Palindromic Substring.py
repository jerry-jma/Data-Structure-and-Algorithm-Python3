# Description
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# Wechat reply question number 200 to get Universal algorithm template . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input:"abcdzdcab"
# Output:"cdzdc"
# Example 2:

# Input:"aba"
# Output:"aba"
# Challenge
# O(n2) time is acceptable. Can you do it in O(n) time.

class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        res = ''
        res_length = 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_length = right - left + 1
                if curr_length > res_length:
                    res_length = right - left + 1
                    res = s[left:right+1]
                left -= 1
                right += 1

            start, end = i, i+1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > res_length:
                    res_length = end - start + 1
                    res = s[start:end+1]
                start -= 1
                end += 1

        return res

