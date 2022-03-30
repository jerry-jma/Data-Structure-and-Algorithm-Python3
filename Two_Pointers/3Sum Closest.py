# Description
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example
# Example 1:

# Input:

# numbers = [2,7,11,15]
# target = 3
# Output:

# 20
# Explanation:

# 2+7+11=20
# Example 2:

# Input:

# numbers = [-1,2,1,-4]
# target = 1
# Output:

# 2
# Explanation:

# -1+2+1=2

# Challenge
# O(n^2)O(n
# 2
#  ) time, O(1)O(1) extra space

from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def three_sum_closest(self, numbers: List[int], target: int) -> int:
        closest_diff = float('inf')
        closest_sum = float('inf')
        numbers.sort()

        for i in range (len(numbers) - 2):
            left, right = i+1, len(numbers)-1

            while left < right:
                three_sum = numbers[i] + numbers[left] + numbers[right]
                if closest_diff >= abs(three_sum-target):
                    closest_diff = abs(three_sum-target)
                    closest_sum = three_sum

                if three_sum > target:
                    right -= 1
                else:
                    left += 1

        return closest_sum