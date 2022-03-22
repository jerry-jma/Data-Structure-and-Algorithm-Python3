# Description
# Given a 2D board and a string word, find if the string word exists in the grid.

# The string word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.

# The same letter cell may not be used more than once.

# The dimension of the letter matrix does not exceed 100, and the length of the string does not exceed 100.

# Example
# Example 1:

# Input:

# board = ["ABCE","SFCS","ADEE"]
# word = "ABCCED"
# Output:

# true
# Explanation:

# [
# A B C E
# S F C S
# A D E E
# ]
# (0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(2,1)

# Example 1:

# Input:

# board = ["z"]
# word = "z"
# Output:

# true
# Explanation:

# [ z ]
# (0,0)

from typing import (
    List,
)
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if word == board[0][0]:
            return True

        if not board or len(board) == 0 or len(board[0]) == 0:
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != word[0]:
                    continue
                if self.search(board, r, c, word, 0, set([(r,c)])):
                    return True

        return  False

    def search(self, board, x, y, word, index, visited):
        print(visited)
        if board[x][y] != word[index]:
            return False
        if index == len(word)-1:
            return True

        for delta_x, delta_y in DIRECTIONS:
            new_x = delta_x + x
            new_y = delta_y + y
            if not self.is_valid(board, new_x, new_y, visited):
                continue

            visited.add((new_x, new_y))
            if self.search(board, new_x, new_y, word, index+1, visited):
                return True
            visited.discard((new_x, new_y))

        return False

    def is_valid(self, board, x, y, visited):
        m = len(board)
        n = len(board[0])

        if not (0 <= x < m and 0 <= y < n):
            return False
        if (x, y) in visited:
            return False

        return True











