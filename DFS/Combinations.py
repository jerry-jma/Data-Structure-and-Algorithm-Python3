# Description
# Given two integers n and k. Return all possible combinations of k numbers out of 1, 2, ... , n.

# You can return all combinations in any order, but numbers in a combination should be in ascending order.

# Example
# Example 1:

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Example 2:

# Input: n = 4, k = 1
# Output: [[1],[2],[3],[4]]

from typing import (
    List,
)

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        self.helper(1, n, k, [], result)

        return result

    def helper(self, index, n, k, combo, result):
        if len(combo) == k:
            result.append(combo[:])
            return

        for i in range(index, n+1):
            combo.append(i)
            self.helper(i+1, n, k, combo, result)
            combo.pop()