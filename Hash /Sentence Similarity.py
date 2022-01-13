# Description
# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

# For example, words1 = great acting skills and words2 = fine drama talent are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

# However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

# 1.The length of words1 and words2 will not exceed 1000.
# 2.The length of pairs will not exceed 2000.
# 3.The length of each pairs[i] will be 2.
# 4.The length of each words[i] and pairs[i][j] will be in the range [1, 20].

# Example
# Example1

# Input: words1 = ["great","acting","skills"], words2 = ["fine","drama","talent"] and pairs = [["great","fine"],["drama","acting"],["skills","talent"]]
# Output: true
# Explanation:
# "great" is similar with "fine"
# "acting" is similar with "drama"
# "skills" is similar with "talent"
# Example2

# Input: words1 = ["fine","skills","acting"], words2 = ["fine","drama","talent"] and pairs = [["great","fine"],["drama","acting"],["skills","talent"]]
# Output: false
# Explanation:
# "fine" is the same as "fine"
# "skills" is not similar with "drama"
# "acting" is not similar with "talent"

class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        # same length, a word is similiar to itself
        if len(words1) != len(words2):
            return False

        hash = {}
        for pair in pairs:
            key = pair[0]
            value = pair[1]
            hash[key] = value

        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]
            if word1 == word2:
                continue
            if word1 in hash and word2 = hash[word1]:
                continue
            if word2 in hash and word1 = hash[word2]:
                continue
            return False

        return True