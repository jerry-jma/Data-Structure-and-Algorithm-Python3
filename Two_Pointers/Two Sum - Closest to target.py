# Description
# Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

# Return the absolute value of difference between the sum of the two numbers and the target.

# Example
# Example1

# Input:  nums = [-1, 2, 1, -4] and target = 4
# Output: 1
# Explanation:
# The minimum difference is 1. (4 - (2 + 1) = 1).
# Example2

# Input:  nums = [-1, -1, -1, -4] and target = 4
# Output: 6
# Explanation:
# The minimum difference is 6. (4 - (- 1 - 1) = 6).
# Challenge
# Do it in O(nlogn) time complexity.

from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def two_sum_closest(self, nums: List[int], target: int) -> int:
        if not nums:
            return

        nums.sort()
        diff = float('inf')
        left, right = 0, len(nums)-1

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum > target:
                right -= 1
                diff = min(diff, abs(target - two_sum))
            else:
                left += 1
                diff = min(diff, abs(target - two_sum))

        return diff
