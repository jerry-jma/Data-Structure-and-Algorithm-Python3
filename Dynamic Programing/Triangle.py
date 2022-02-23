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


        # solution 2: using DP
    def minimum_total(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return -1

        n = len(triangle)
        dp = [[0]*n for _ in range(n)]

        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
            print(i, i-1)
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

        return min(dp[n-1])


    def minimum_total(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return -1
        n = len(triangle)
        dp = [[0] * n, [0]*n]

        dp[0][0] = triangle[0][0]

        for row in range(1, n):
            dp[row%2][0] = dp[(row-1)%2][0] + triangle[row][0]
            dp[row%2][row] = dp[(row-1)%2][row-1] + triangle[row][row]
            for col in range(1, row):
                dp[row%2][col] = min(dp[(row-1)%2][col], dp[(row-1)%2][col-1]) + triangle[row][col]

        return min(dp[(n-1)%2])


