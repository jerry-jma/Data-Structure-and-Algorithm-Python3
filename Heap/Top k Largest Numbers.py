# Description
# Given an integer array, find the top k largest numbers in it.

# Example
# Example1

# Input: [3, 10, 1000, -99, 4, 100] and k = 3
# Output: [1000, 100, 10]
# Example2

# Input: [8, 7, 6, 5, 4, 3, 2, 1] and k = 5
# Output: [8, 7, 6, 5, 4]

from typing import (
    List,
)

import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    Solution 1: Min Heap
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for _ in range(k):
            val = heapq.heappop(heap)
            result.append(val)

        result.reverse()

        return result

    Solution 2: Quick Select
    def topk(self, nums: List[int], k: int) -> List[int]:

# Solution 2: Quick Select
    # Note: quick select won't sort the entire array
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        k = len(nums) - k
        self.quick_select(nums, 0, len(nums)-1, k)

        result = nums[k:]
        # Note: quick select won't sort the entire array
        # that's why we need sort the sliced result in reverse order
        result.sort(reverse=True)

        return result

    def quick_select(self, nums, start, end, k):
        if start == end:
            return

        left, right = start, end
        mid = (start + end) // 2
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

