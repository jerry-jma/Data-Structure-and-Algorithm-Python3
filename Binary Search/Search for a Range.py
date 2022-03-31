# Description
# Given a sorted array of n integers, find the starting and ending position of a given target value.

# If the target is not found in the array, return [-1, -1].

# Example
# Example 1:

# Input:

# array = []
# target = 9
# Output:

# [-1,-1]
# Explanation:

# 9 is not in the array.

# Example 2:

# Input:

# array = [5, 7, 7, 8, 8, 10]
# target = 8
# Output:

# [3,4]
# Explanation:

# The [3,4] subinterval of the array 1 has the value 8.

# Challenge
# O(log n) time.

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def search_range(self, a: List[int], target: int) -> List[int]:
        if not a:
            return [-1, -1]

        left = self.find_first_position(a, target)
        right = self.find_last_position(a, target)

        return [left, right]

    def find_first_position(self, a, target):
        start, end = 0, len(a) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if a[mid] > target:
                end = mid
            elif a[mid] < target:
                start = mid
            else:
                end = mid

        if a[start] == target:
            return start
        if a[end] == target:
            return end
        return -1

    def find_last_position(self, a, target):
        start, end = 0, len(a) - 1

        while start + 1 < end:
            mid = start + (end-start) // 2
            if a[mid] > target:
                end = mid
            elif a[mid] < target:
                start = mid
            else:
                start = mid

        if a[end] == target:
            return end
        if a[start] == target:
            return start
        return -1




