# Description
# Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
# Transformation rule such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
# Wechat reply question number 120 to get Universal algorithm template . (wechat id : jiuzhang15)

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the dictionary.
# You may assume beginWord and endWord are non-empty and are not the same.
# len(dict) <= 5000, len(start) < 5len(dict)<=5000,len(start)<5
# Example
# Example 1:

# Input:

# start = "a"
# end = "c"
# dict =["a","b","c"]
# Output:

# 2
# Explanation:

# "a"->"c"

# Example 2:

# Input:

# start ="hit"
# end = "cog"
# dict =["hot","dot","dog","lot","log"]
# Output:

# 5
# Explanation:

# "hit"->"hot"->"dot"->"dog"->"cog"

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        # BFS not care about levels
        # distance = {start: 1}

        # while queue:
        #     word = queue.popleft()
        #     if word == end:
        #         return distance[word]
        #     for next_word in self.get_next_words(word, dict):
        #         print(next_word)
        #         # distance[next_word] = distance.get(next_word, 0) + 1
        #         # if next_word == end:
        #         #     return distance[next_word]
        #         if next_word in distance:
        #             continue
        #         queue.append(next_word)
        #         distance[next_word] = distance[word] + 1

        # BFS by levels
        visited =set([start])
        distance = 0

        while queue:
            distance += 1
            length = len(queue)
            for i in range(length):
                curr_word = queue.popleft()
                if curr_word == end:
                    return distance
                for next_word in self.get_next_words(curr_word, dict):
                    if next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)

        return 0

    def get_next_words(self, word, dict):
        next_words = []

        for i in range(len(word)):
            left = word[0:i]
            right = word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]:
                    continue
                possible_match = left + char + right
                # note find a string in dict is not o(n), find an integer in map is o(1)
                if possible_match in dict:
                    next_words.append(possible_match)
        print(next_words)
        return next_words




