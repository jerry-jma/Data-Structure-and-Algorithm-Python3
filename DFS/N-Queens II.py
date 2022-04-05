# Description
# According to N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.

# n <= 10n<=10

# Example
# Example 1:

# Input:

# n = 1
# Output:

# 1
# Explanation:

# 1:
# 1

# Example 2:

# Input:

# n = 4
# Output:

# 2
# Explanation:

# 1:
# 0 0 1 0
# 1 0 0 0
# 0 0 0 1
# 0 1 0 0
# 2:
# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def total_n_queens(self, n: int) -> int:
        board = [['.'] * n for i in range(n)]
        result = []
        visited = {
            'col_set': set(),
            'pos_diag': set(),
            'neg_diag': set(),
        }
        self.search(0, n, board, result, visited)
        return len(result)

    def search(self, curr_row, n, board, result, visited):
        if curr_row == n:
            # could simply use a global variable to track the numbers of answers
            # it's just for practice to write like this
            copy = [''.join(row_arr) for row_arr in board]
            result.append(copy);
            return

        for curr_col in range(n):
            if not self.is_valid(curr_row, curr_col, visited):
                continue

            board[curr_row][curr_col] = 'Q'
            visited['col_set'].add(curr_col)
            visited['pos_diag'].add(curr_row+curr_col)
            visited['neg_diag'].add(curr_row-curr_col)

            self.search(curr_row+1, n, board, result, visited)

            visited['neg_diag'].remove(curr_row-curr_col)
            visited['pos_diag'].remove(curr_row+curr_col)
            visited['col_set'].remove(curr_col)
            board[curr_row][curr_col] = '.'

    def is_valid(self, curr_row, curr_col, visited):
        if curr_col in visited['col_set']:
            return False

        if curr_row + curr_col in visited['pos_diag']:
            return False

        if curr_row - curr_col in visited['neg_diag']:
            return False

        return True





