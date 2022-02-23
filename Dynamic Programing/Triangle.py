# Description
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# Wechat reply the 【109】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Bonus point if you are able to do this using only O(n)O(n) extra space, where n is the total number of rows in the triangle.

# Example
# Example 1:

# Input:

# triangle = [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# Output:

# 11
# Explanation:

# The minimum path sum from top to bottom is 11 (2 + 3 + 5 + 1 = 11).

# Example 2:

# Input:

# triangle = [
#      [2],
#     [3,2],
#    [6,5,7],
#   [4,4,8,1]
# ]
# Output:

# 12
# Explanation:

# The minimum path sum from top to bottom is 12 (2 + 2 + 7 + 1 = 12).

from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    # Possible solutions: DFS traverse and divide conquer \
    # is not ideal when data is very large O(2^n)

    #  divide & conquer with hashmap can work, but pretty slow
    # def minimum_total(self, triangle: List[List[int]]) -> int:
    #     return self.divide_conquer(triangle, 0, 0, {})

    # def divide_conquer(self, triangle, x, y, memo):
    #     if x == len(triangle):
    #         return 0

    #     if (x,y) in memo:
    #         return memo[(x,y)]

    #     left = self.divide_conquer(triangle, x+1, y, memo)
    #     right = self.divide_conquer(triangle, x+1, y+1, memo)

    #     memo[(x,y)] = min(left, right) + triangle[x][y]

    #     return memo[(x,y)]


    def minimum_total(self, triangle: List[List[int]]) -> int:


