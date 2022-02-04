# Description
# Find any position of a target number in a sorted array. Return -1 if target does not exist.

# Wechat reply 【457】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input: nums = [1,2,2,4,5,5], target = 2
# Output: 1 or 2
# Example 2:

# Input: nums = [1,2,2,4,5,5], target = 6
# Output: -1
# Challenge
# O(logn) time


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums)

        while start + 1 < end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid
            else:
                return mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1