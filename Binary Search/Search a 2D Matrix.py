# Description
# Write an efficient algorithm that searches for a target value in an m x n matrix.

# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# n × m < 50000n×m<50000

# Example
# Example 1:

# Input:

# matrix = [[5]]
# target = 2
# Output:

# false
# Explanation:

# The matrix does not include 2 , returns false.

# Example 2:

# Input:

# matrix = [
#   [1, 3, 5, 7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output:

# true
# Explanation:

# The matrix includes 3, return true.

# Challenge
# O(log(n) + log(m)) time


from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])

        start = 0
        end = row_len * col_len - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if self.getValue(matrix, mid) > target:
                end = mid
            else:
                start = mid
        if self.getValue(matrix, start) == target:
            return True
        if self.getValue(matrix, end) == target:
            return True

        return False

    def getValue(self, matrix, number):
        col_len = len(matrix[0])

        x = number // col_len
        y = number % col_len

        return matrix[x][y]
