# Description
# Find the kth smallest number in an unsorted integer array (K start at 1).

# Example
# Example 1:

# Input: [3, 4, 1, 2, 5], k = 3
# Output: 3
# Example 2:

# Input: [1, 1, 1], k = 2
# Output: 1
# Challenge
# An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.


from typing import (
    List,
)

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kth_smallest(self, k: int, nums: List[int]) -> int:
        self.quick_select(nums, 0, len(nums)-1, k-1)
        return nums[k-1]

    def quick_select(self, nums, start, end, k):
        # exit
        if start == end:
            return

        left, right = start, end
        mid = (start+end) // 2
        pivot = nums[mid]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            self.quick_select(nums, start, right, k)
        if k >= left:
            self.quick_select(nums, left, end, k)






