# Description
# Given an integer matrix. Find the longest increasing continuous subsequence in this matrix and return the length of it.

# The longest increasing continuous subsequence here can start at any position and go up/down/left/right.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Example
# Example 1:

# Input:
#     [
#       [1, 2, 3, 4, 5],
#       [16,17,24,23,6],
#       [15,18,25,22,7],
#       [14,19,20,21,8],
#       [13,12,11,10,9]
#     ]
# Output: 25
# Explanation: 1 -> 2 -> 3 -> 4 -> 5 -> ... -> 25 (Spiral from outside to inside.)
# Example 2:

# Input:
#     [
#       [1, 2],
#       [5, 3]
#     ]
# Output: 4
# Explanation: 1 -> 2 -> 3 -> 5
# Challenge
# Assume that it is a N x M matrix. Solve this problem in O(NM) time and memory.


from typing import (
    List,
)
DIRECTIONS = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]
class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longest_continuous_increasing_subsequence2(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        row_len = len(matrix)
        col_len = len(matrix[0])

        points = []

        for i in range(row_len):
            for j in range(col_len):
                points.append((matrix[i][j], i, j))

        points.sort()

        longest_hash = {}

        for i in range(len(points)):
            key = (points[i][1], points[i][2])
            longest_hash[key] = 1

            for x, y in DIRECTIONS:
                neighbor_x = x + points[i][1]
                neighbor_y = y + points[i][2]

                if not(0 <= neighbor_x < row_len and 0 <= neighbor_y < col_len):
                    continue
                # 从小到大loop，之前的数一定在longest_hash 里面
                if (neighbor_x, neighbor_y) in longest_hash and \
                    matrix[neighbor_x][neighbor_y] < points[i][0]:
                    print('hi', longest_hash[key], longest_hash[(neighbor_x, neighbor_y)])
                    longest_hash[key] = max(longest_hash[key], longest_hash[(neighbor_x, neighbor_y)] + 1)

        return max(longest_hash.values())
