# Description
# Given an sorted array of integers, find two numbers that their difference equals to a target value.
# Return a list with two number like [num1, num2] that the difference of num1 and num2 equals to target value, and num1 is less than num2.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# It's guaranteed there is only one available solution.
# Note: Requires O(1) space complexity to comple

# Example
# Example 1:

# Input: nums = [2, 7, 15, 24], target = 5
# Output: [2, 7]
# Explanation:
# (7 - 2 = 5)
# Example 2:

# Input: nums = [1, 1], target = 0
# Output: [1, 1]
# Explanation:
# (1 - 1 = 0)
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    # solution 1: using binary search O(nlogn)
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        target = abs(target)
        for i in range(len(nums)):
            j = self.binary_search(nums, i+1, len(nums)-1, target+nums[i])
            if j != -1:
                return [nums[i], nums[j]]

        return [-1, -1]

    def binary_search(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                return mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    # solution 2: better solution, two pointers 同向双指针
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        target = abs(target)
        j = 1
        for i in range(len(nums)):
            if i == j:
                j += 1
            while j < len(nums) and nums[j] - nums[i] < target:
                j += 1
            if j >= len(nums):
                break
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]

        return [-1, -1]
