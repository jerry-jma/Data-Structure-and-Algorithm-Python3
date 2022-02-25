# Description
# Write an efficient algorithm that searches for a value in an m x n matrix, return The number of occurrence of it.

# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# Integers in each column are sorted from up to bottom.
# No duplicate integers in each row or column.
# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Example
# Example 1:

# Input:

# matrix = [[3,4]]
# target = 3
# Output:

# 1
# Explanation:

# There is only one 3 in the matrix.

# Example 2:

# Input:

# matrix = [
#       [1, 3, 5, 7],
#       [2, 4, 7, 8],
#       [3, 5, 9, 10]
#     ]
# target = 3
# Output:

# 2
# Explanation:

# There are two 3 in the matrix.

# Challenge
# O(m+n) time and O(1) extra space

from typing import (
    List,
)

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0

        row_len = len(matrix)
        col_len = len(matrix[0])

        x = row_len - 1
        y = 0
        counter = 0

        while (x >= 0 and y < col_len):
            if matrix[x][y] == target:
                x -= 1
                y += 1
                counter += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1

        return counter