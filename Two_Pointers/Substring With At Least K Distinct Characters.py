# Description
# Given a string S with only lowercase characters.

# Return the number of substrings that contains at least k distinct characters.

# 10 ≤ length(S) ≤ 1,000,00010≤length(S)≤1,000,000
# 1 ≤ k ≤ 261≤k≤26
# Example
# Example 1:

# Input: S = "abcabcabca", k = 4
# Output: 0
# Explanation: There are only three distinct characters in the string.
# Example 2:

# Input: S = "abcabcabcabc", k = 3
# Output: 55
# Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
#     For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
#     There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
#     ...
#     There is 1 substring whose length is 12, "abcabcabcabc"
#     So the answer is 1 + 2 + ... + 10 = 55.

class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def k_distinct_characters(self, s: str, k: int) -> int:
        char_count = {}
        fast = 0
        total = 0

        for slow in range(len(s)):
            while len(char_count) < k and fast < len(s):
                curr_char = s[fast]
                char_count[curr_char] = char_count.get(curr_char, 0) + 1
                fast += 1

            if len(char_count) == k:
                total += (len(s) - 1) - (fast - 1) + 1

            char_count[s[slow]] -= 1
            if char_count[s[slow]] == 0:
                del char_count[s[slow]]

        return total

