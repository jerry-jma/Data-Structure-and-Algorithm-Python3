# Description
# Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Both the string's length and k will not exceed 10^4.

# Example
# Example1

# Input:
# "ABAB"
# 2
# Output:
# 4
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# Example2

# Input:
# "AABABBA"
# 1
# Output:
# 4
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        counter = {}
        slow = 0
        res = 0

        for fast in range(len(s)):
            counter[s[fast]] = counter.get(s[fast], 0) + 1
            while fast - slow + 1 - max(counter.values()) > k:
                counter [s[slow]] -= 1
                slow += 1

            res = max(res, fast - slow + 1)

        return res