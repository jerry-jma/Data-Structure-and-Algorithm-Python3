# Description
# The N-queens puzzle is the problem of placing n queens on an n×nn×n chessboard, and the queens can not(Any two queens can't be in the same row, column, diagonal line).Given an integer n, return all distinct solutions to the N-queens puzzle.Each solution contains a distinct board configuration of the N-queens' placement, where 'Q' and '.' each indicate a queen and an empty space respectively.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# n <= 10n<=10

# Example
# Example 1:

# Input:

# n = 1
# Output:

# [["Q"]]
# Explanation:

# There is only one solution.

# Example 2:

# Input:

# n = 4
# Output:

# [
#   // Solution 1
#   [".Q..",
#    "...Q",
#    "Q...",
#    "..Q."
#   ],
#   // Solution 2
#   ["..Q.",
#    "Q...",
#    "...Q",
#    ".Q.."
#   ]
# ]
# Explanation:

# There are two solutions.

# Challenge
# Can you do it without recursion?

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    # solution 1
    # def solveNQueens(self, n):
    #     boards = []
    #     visited = {
    #         'col_set': set(),
    #         'pos_diag': set(),
    #         'neg_diag': set(),
    #     }
    #     self.dfs(n, [], visited, boards)
    #     return boards

    # def dfs(self, n, combo, visited, boards):
    #     if len(combo) == n:
    #         boards.append(self.draw(combo))

    #     row = len(combo)
    #     for col in range(n):
    #         if not self.isValid(visited, combo, col):
    #             continue
    #         combo.append(col)
    #         visited['col_set'].add(col)
    #         visited['pos_diag'].add(row + col)
    #         visited['neg_diag'].add(row - col)

    #         self.dfs(n, combo, visited, boards)

    #         combo.pop()
    #         visited['col_set'].remove(col)
    #         visited['pos_diag'].remove(row + col)
    #         visited['neg_diag'].remove(row - col)

    # def draw(self, combo):
    #     board = []
    #     n = len(combo)
    #     for col in combo:
    #         row_string = ['Q' if c == col else '.' for c in range(n)]
    #         board.append(''.join(row_string))
    #     return board

    # def isValid(self, visited, combo, col):
    #     row = len(combo)
    #     if col in visited['col_set']:
    #         return False
    #     if row + col in visited['pos_diag']:
    #         return False
    #     if row - col in visited['neg_diag']:
    #         return False
    #     return True

    def solveNQueens(self, n):
        board = [['.'] * n for i in range(n)]
        result = []
        visited = {
            'col_set': set(),
            'pos_diag': set(),
            'neg_diag': set(),
        }
        self.dfs(n, 0, board, visited, result)
        return result

    def dfs(self, n, curr_row, board, visited, result):
        if curr_row == n:
            copy = [''.join(r) for r in board]
            result.append(copy)

        for col in range(n):
            if not self.isValid(visited, board, curr_row, col):
                continue
            board[curr_row][col] = 'Q'
            visited['col_set'].add(col)
            visited['pos_diag'].add(curr_row + col)
            visited['neg_diag'].add(curr_row - col)

            self.dfs(n, curr_row + 1, board, visited, result)

            board[curr_row][col] = '.'
            visited['col_set'].remove(col)
            visited['pos_diag'].remove(curr_row + col)
            visited['neg_diag'].remove(curr_row - col)

    def isValid(self, visited, board, curr_row, col):
        if col in visited['col_set']:
            return False
        if curr_row + col in visited['pos_diag']:
            return False
        if curr_row - col in visited['neg_diag']:
            return False
        return True