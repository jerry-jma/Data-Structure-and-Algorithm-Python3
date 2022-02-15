# Description
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Wechat reply 【539】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Example
# Example 1:

# Input: nums = [0, 1, 0, 3, 12],
# Output: [1, 3, 12, 0, 0].
# Example 2:

# Input: nums = [0, 0, 0, 3, 1],
# Output: [3, 1, 0, 0, 0].

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        if not nums:
            return nums

        slow, fast = 0, 0

        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
                continue
            else:
                # only cover the value, no swaping
                nums[slow] = nums[fast]
                slow += 1
                fast += 1

        while slow < len(nums):
            nums[slow] = 0
            slow += 1


