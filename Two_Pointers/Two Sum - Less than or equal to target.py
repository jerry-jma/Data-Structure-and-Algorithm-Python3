# Description
# Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

# Example
# Example 1:

# Input: nums = [2, 7, 11, 15], target = 24.
# Output: 5.
# Explanation:
# 2 + 7 < 24
# 2 + 11 < 24
# 2 + 15 < 24
# 7 + 11 < 24
# 7 + 15 < 24
# Example 2:

# Input: nums = [1], target = 1.
# Output: 0.

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        left = 0
        right = len(nums)-1
        total = 0

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum <= target:
                total += right - left
                left += 1
            else:
                right -= 1

        return total