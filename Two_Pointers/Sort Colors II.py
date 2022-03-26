# Description
# Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

# You are not suppose to use the library's sort function for this problem.
# k <= n
# Example
# Example1

# Input:
# [3,2,2,1,4]
# 4
# Output:
# [1,2,2,3,4]
# Example2

# Input:
# [2,1,1,2,2]
# 2
# Output:
# [1,1,2,2,2]
# Challenge
# You can directly use The counting sorting algorithm scan twice, but it will cost O(k) extra memory. Now can you do it in use O(logk) extra memory?

from typing import (
    List,
)

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        if not colors:
            return

        self.sort_colors2_helper(colors, 1, k, 0, len(colors)-1)

    def sort_colors2_helper(self, colors, start_color, end_color, start_idx, end_idx):
        if start_color == end_color:
            return

        pivot_color = (start_color + end_color) // 2
        left, right = start_idx, end_idx

        while left <= right:
            while left <= right and colors[left] <= pivot_color:
                left += 1
            while left <= right and colors[right] > pivot_color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.sort_colors2_helper(colors, start_color, pivot_color, start_idx, right)
        self.sort_colors2_helper(colors, pivot_color+1, end_color, left, end_idx)


