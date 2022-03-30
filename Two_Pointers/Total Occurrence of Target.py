# Description
# Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

# Example
# Example1:

# Input: [1, 3, 3, 4, 5] and target = 3,
# Output: 2.
# Example2:

# Input: [2, 2, 3, 4, 6] and target = 4,
# Output: 1.
# Example3:

# Input: [1, 2, 3, 4, 5] and target = 6,
# Output: 0.
# Challenge
# Time complexity in O(logn)

from typing import (
    List,
)

class Solution:
    """
    @param a: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def total_occurrence(self, a: List[int], target: int) -> int:
        if not a:
            return 0

        last_position = self.binary_search_last_position(a, target)
        first_position = self.binary_search_first_position(a, target)

        # if the target exists, both indexes must greater than 0

        if last_position >= 0 and first_position >= 0:
            return last_position - first_position + 1

        return 0

    def binary_search_last_position(self, a, target):
        start, end = 0, len(a) - 1

        while start + 1 < end:
            mid = (start+end) // 2
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

    def binary_search_first_position(self, a, target):
        start, end = 0, len(a) - 1

        while start + 1 < end:
            mid = (start+end) // 2
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




















