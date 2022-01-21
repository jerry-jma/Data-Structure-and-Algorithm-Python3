# Description
# Given an input string, reverse the string word by word.

# Wechat reply the 【53】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# What constitutes a word?
# A sequence of non-space characters constitutes a word and some words have punctuation at the end.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.
# Example
# Example 1:

# Input:

# s = "the sky is blue"
# Output:

# "blue is sky the"
# Explanation:

# return a reverse the string word by word.
# Example 2:

# Input:

# s = "hello world"
# Output:

# "world hello"
# Explanation:

# return a reverse the string word by word.


class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        # converted into array without space
        # loop over backwards and push into a new result
        # converted = s.split(' ')
        # result = []
        # for i in range(len(converted) - 1, -1, -1):
        #     if len(converted[i]) == 0:
        #         continue
        #     result.append(converted[i])
        # return ' '.join(result)

        # converted_array = reversed(s.split())

        converted = s.split()
        converted.reverse()
        return ''.join(converted)