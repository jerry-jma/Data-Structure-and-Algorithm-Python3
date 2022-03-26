# Description
# Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?

# Example
# Example 1:

# Input: [3, 4, 6, 7]
# Output: 3
# Explanation:
# They are (3, 4, 6),
#          (3, 6, 7),
#          (4, 6, 7)
# Example 2:

# Input: [4, 4, 4, 4]
# Output: 4
# Explanation:
# Any three numbers can form a triangle.
# So the answer is C(3, 4) = 4

from typing import (
    List,
)

class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s: List[int]) -> int:
        if not s or len(s) < 3:
            return 0

        counter = 0
        s.sort()

        for i in range(2, len(s)):
            counter += self.get_triangle_count(s, i)

        return counter

    def get_triangle_count(self, nums, target_index):
        left = 0
        right = target_index - 1
        target = nums[target_index]

        temp = 0

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum > target:
                temp += right - left
                right -= 1
            else:
                left += 1

        return temp









