# Description
# Given an array of strings, return all groups of strings that are anagrams.If a string is Anagram,there must be another string with the same letter set but different order in S.

# All inputs will be in lower-case

# Example
# Example 1:

# Input:["lint", "intl", "inlt", "code"]
# Output:["lint", "inlt", "intl"]
# Example 2:

# Input:["ab", "ba", "cd", "dc", "e"]
# Output: ["ab", "ba", "cd", "dc"]
# Challenge
# What is Anagram?

# Two strings are anagram if they can be the same after change the order of characters.


from typing import (
    List,
)

class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs: List[str]) -> List[str]:
        tracker = collections.defaultdict(list)
        result = []

        for string in strs:
            sorted_string = ''.join(sorted(string))
            # if... else is not necessary here since we use defaultdict
            tracker[sorted_string].append(string)

        for arr in tracker.values():
            if len(arr) >= 2:
                result += arr

        return result
