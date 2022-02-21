# Description
# Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

# Wechat reply the 【683】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Ignore case

# Example
# Example1

# Input:
# "CatMat"
# ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
# Output: 3
# Explanation:
# we can form 3 sentences, as follows:
# "CatMat" = "Cat" + "Mat"
# "CatMat" = "Ca" + "tM" + "at"
# "CatMat" = "C" + "at" + "Mat"
# Example1

# Input:
# "a"
# []
# Output:
# 0


from typing import (
    Set,
)

class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def word_break3(self, s: str, dict: Set[str]) -> int:
        if not s or not dict:
            return 0

        max_len = len(max(dict, key=len))

        lower_dict = set()
        for word in dict:
            lower_dict.add(word.lower())

        lower_s = s.lower()
        return self.dfs(lower_s, 0, max_len, lower_dict, {})

    def dfs(self, s, index, max_len, lower_dict, memo):
        if index == len(s):
            return 1

        if index in memo:
            return memo[index]

        result = 0

        # to ensure it has at least one char when slicing
        for end in range(index+1, len(s)+1):
            if end - index > max_len:
                break

            word = s[index:end]

            if word not in lower_dict:
                continue

            result += self.dfs(s, end, max_len, lower_dict, memo)

        memo[index] = result

        return result
