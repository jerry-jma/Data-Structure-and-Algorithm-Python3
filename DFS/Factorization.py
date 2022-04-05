# Description
# A non-negative numbers can be regarded as product of its factors.
# Write a function that takes an integer n and return all possible combinations of its factors.

# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combination.
# Example
# Example1

# Input: 8
# Output: [[2,2,2],[2,4]]
# Explanation:
# 8 = 2 x 2 x 2 = 2 x 4
# Example2

# Input: 1
# Output: []

from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    # will got runtime error
    def get_factors(self, n: int) -> List[List[int]]:
        result = []
        self.helper(2, n, [], result)
        return result

    def helper(self, start, remainder, path, result):
        # 为了得到[2,2,2]也要得到[2,4]，4就是还未被分解的reminder.
        # 先append再pop是为了保持path不变，
        # 也可以把三行代码写成result.append(path[:] + [reminder])
        if path:
                path.append(remainder)
                result.append(path[:])
                path.pop()

        for i in range(start, int(math.sqrt(remainder))+1):
            if remainder % i == 0:
                path.append(i)
                self.helper(i, int(remainder/i), path, result)
                path.pop()

