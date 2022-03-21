# Description
# Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word. No same word in dictionary

# Example
# Example 1:

# Input：["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
# Output：["again","can","dad","dog"]
# Explanation：
#   d o a f
#   a g a i
#   d c a n
# search in Matrix，so return ["again","can","dad","dog"].
# Example 2:

# Input：["a"]，["b"]
# Output：[]
# Explanation：
#  a
# search in Matrix，return [].
# Challenge
# Using trie to implement your algorithm.

DIRECTIONS = [
    (0,1),
    (0,-1),
    (1, 0),
    (-1,0),
]
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if not board or not board[0]:
            return []
        prefix_set = set()
        word_set = set(words)
        result = set()

        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[0:i+1])

        for r in range(len(board)):
            for c in range(len(board[0])):
                self.search(
                    board,
                    r,
                    c,
                    board[r][c],
                    prefix_set,
                    word_set,
                    set([(r, c)]),
                    result)

        return list(result)

    def search(
        self,
        board,
        x,
        y,
        word,
        prefix_set,
        word_set,
        visited,
        result
    ):
        if word not in prefix_set:
            return

        if word in word_set:
            result.add(word)

        for delta_x, delta_y in DIRECTIONS:
            new_x = delta_x + x
            new_y = delta_y + y

            if not self.is_valid(board, new_x, new_y, visited):
                continue

            visited.add((new_x, new_y))

            self.search(
                board,
                new_x,
                new_y,
                word + board[new_x][new_y],
                prefix_set,
                word_set,
                visited,
                result
            )

            visited.discard((new_x, new_y))

    def is_valid(self, board, x, y, visited):
        m = len(board)
        n = len(board[0])

        if not (0 <= x < m and 0 <= y < n):
            return False
        if (x,y) in visited:
            return False

        return True














