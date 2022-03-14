# Description
# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)


# Example
# Example 1
# Input: “eceba”
# Output: 3
# Explanation:
# T is "ece" which its length is 3.
# Example 2
# Input: “aaa”
# Output: 3

class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s:
            return 0
        slow = 0
        fast = 0
        max_len = 0
        # {char: index}, should always check and should less than 2
        char_idx_dict = {}

        while fast < len(s):
            char_idx_dict[s[fast]] = fast
            if len(char_idx_dict) > 2:
                earliest_idx = min(char_idx_dict.values())
                slow = earliest_idx + 1
                del char_idx_dict[s[earliest_idx]]

            max_len = max(max_len, fast - slow + 1)
            fast += 1

        return max_len