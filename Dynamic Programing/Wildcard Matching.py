# Description
# Implement wildcard pattern matching with support for '?' and '*'.The matching rules are as follows：

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Wechat reply the 【192】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# 0 <= |s|, |p| <= 1000
# It is guaranteed that 𝑠 only contains lowercase Latin letters and p contains lowercase Latin letters , ? and *

# Example
# Example 1

# Input:
# "aa"
# "a"
# Output: false
# Example 2

# Input:
# "aa"
# "aa"
# Output: true
# Example 3

# Input:
# "aaa"
# "aa"
# Output: false
# Example 4

# Input:
# "aa"
# "*"
# Output: true
# Explanation: '*' can replace any string
# Example 5

# Input:
# "aa"
# "a*"
# Output: true
# Example 6

# Input:
# "ab"
# "?*"
# Output: true
# Explanation: '?' -> 'a' '*' -> 'b'
# Example 7

# Input:
# "aab"
# "c*a*b"
# Output: false


class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        if s is None or p is None:
            return False

        return self.is_match_helper(s, 0, p, 0, {})

    def is_match_helper(self, source, s_index, pattern, p_index, memo):
        if s_index == len(source):
            return self.is_all_stars(pattern, p_index)

        if p_index == len(pattern):
            return s_index == len(source)

        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]

        s_char = source[s_index]
        p_char = pattern[p_index]
        match = False

        if p_char != '*':
            match = self.is_char_match(s_char, p_char) and \
                self.is_match_helper(source, s_index+1, pattern, p_index+1, memo)

        # for new_index in range(s_index, len(source)+1):
        #     if self.is_match_helper(source, new_index, pattern, p_index+1):
        #         return True
        else:
            match = self.is_match_helper(source, s_index+1, pattern, p_index, memo) or \
                self.is_match_helper(source, s_index, pattern, p_index+1, memo)

        memo[(s_index, p_index)] = match
        return match
        # return False

    def is_char_match(self, s_char, p_char):
        return s_char == p_char or p_char == '?'

    def is_all_stars(self, pattern, p_index):
        for i in range(p_index, len(pattern)):
            if pattern[i] != '*':
                return False
        return True