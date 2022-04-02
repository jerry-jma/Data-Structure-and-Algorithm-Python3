# Description
# Given a string s and a set of n substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.

# Example
# Example 1:

# Input:
# "ccdaabcdbb"
# ["ab","cd"]
# Output:
# 2
# Explanation:
# ccdaabcdbb -> ccdacdbb -> cacdbb -> cabb -> cb (length = 2)
# Example 2:

# Input:
# "abcabd"
# ["ab","abcd"]
# Output:
# 0
# Explanation:
# abcabd -> abcd -> "" (length = 0)

from typing import (
    Set,
)

class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def min_length(self, s: str, dict: Set[str]) -> int:
        queue = collections.deque([s])
        visited = set([s])
        min_length = len(s)

        while queue:
            curr_str = queue.popleft()

            min_length = min(min_length, len(curr_str))

            for word in dict:
                found_idx = curr_str.find(word)
                while found_idx != -1:
                    # to found all the word appear in the curr_str
                    # then create a new string taking out the word
                    # from curr_str, not the original string
                    udpated_str = curr_str[:found_idx] + curr_str[found_idx+len(word):]

                    if udpated_str not in visited:
                        queue.append(udpated_str)
                        visited.add(udpated_str)

                    found_idx = curr_str.find(word, found_idx+1)

        return min_length


