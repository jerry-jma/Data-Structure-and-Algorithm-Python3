# Description
# Given a collection of integers that might contain duplicate numbers, return all possible subsets.

# Each element in a subset must be in non-descending order.
# The ordering between two subsets is free.
# The solution set must not contain duplicate subsets.
# Example
# Example 1:

# Input:

# nums = [0]
# Output:

# [
#   [],
#   [0]
# ]
# Explanation:

# The subsets of [0] are only [] and [0].

# Example 2:

# Input:

# nums = [1,2,2]
# Output:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# Explanation:

# The distinct subsets of [1,2,2] are [], [1], [2], [1,2], [2,2], [1,2,2].

# Challenge
# Can you do it in both recursively and non-recursively?

from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        nums.sort()
        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, index, subset, result):
        result.append(subset[:])

        for i in range(index, len(nums)):
            if i > index and nums[i-1] == nums[i]: #这里是i > index
                continue

            subset.append(nums[i])
            self.dfs(nums, i+1, subset, result)
            subset.pop()