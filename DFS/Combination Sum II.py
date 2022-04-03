# Description
# Given an array num and a number target. Find all unique combinations in num where the numbers sum to target.

# Each number in num can only be used once in one combination.
# All numbers (including target) will be positive integers.
# Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
# Different combinations can be in any order.
# The solution set must not contain duplicate combinations.
# Example
# Example 1:

# Input: num = [7,1,2,5,1,6,10], target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
# Example 2:

# Input: num = [1,1,1], target = 2
# Output: [[1,1]]
# Explanation: The solution set must not contain duplicate combinations.


from typing import (
    List,
)

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combination_sum2(self, num: List[int], target: int) -> List[List[int]]:
        if not num:
            return []

        num.sort()
        result = []
        self.helper(num, 0, target, [], result)
        return result

    def helper(self, num, index, target, combo, result):
        if target == 0:
            result.append(combo[:])
            return
        if target < 0:
            return

        for i in range(index, len(num)):
            if i > index and num[i] == num[i-1]:
                continue

            combo.append(num[i])
            self.helper(num, i+1, target-num[i], combo, result)
            combo.pop()


