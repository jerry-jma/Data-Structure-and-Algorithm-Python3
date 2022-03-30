# Description
# Given two arrays, write a function to compute their intersection.

# Each element in the result must be unique.
# Example
# Example 1:

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2],
# Output: [2].
# Example 2:

# Input: nums1 = [1, 2], nums2 = [2],
# Output: [2].
# Challenge
# Can you implement it in three different algorithms?

from typing import (
    List,
)

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    # Solution 1: hashset
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = []

        for num in nums2:
            if num in set1:
                result.append(num)
                set1.discard(num)

        return result




    # Solution 2: two pointers
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []

        index_1, index_2 = 0, 0

        while index_1 < len(nums1) and index_2 < len(nums2):
            if nums1[index_1] == nums2[index_2]:
                result.append(nums1[index_1])
                index_1 += 1
                index_2 += 1

                while index_1 < len(nums1) and nums1[index_1] == nums1[index_1 - 1]:
                    index_1 += 1
                while index_2 < len(nums2) and nums2[index_2] == nums2[index_2 - 1]:
                    index_2 += 1

            elif nums1[index_1] < nums2[index_2]:
                index_1 += 1
            else:
                index_2 += 1

        return result