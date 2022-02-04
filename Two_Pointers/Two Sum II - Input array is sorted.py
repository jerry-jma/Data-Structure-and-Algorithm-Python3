# Description
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# Wechat reply 【608】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# You may assume that each input would have exactly one solution.

# Example
# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# Example 2:

# Input: nums = [2,3], target = 5
# Output: [1, 2]

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if not nums:
            return None

        left, right = 0, len(nums) - 1

        while left <= right:
            curr_sum = nums[left] + nums[right]
            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return None

