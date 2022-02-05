# Description
# Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

# Wechat reply 【587】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input: nums = [1,1,2,45,46,46], target = 47
# Output: 2
# Explanation:

# 1 + 46 = 47
# 2 + 45 = 47
# Example 2:

# Input: nums = [1,1], target = 2
# Output: 1
# Explanation:
# # 1 + 1 = 2

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    # solution 1: hashmap, if used = 1, not used 0, should check before add
    # def twoSum6(self, nums, target):
    #     if not nums or len(nums) <= 1:
    #         return 0
    #     tracker = {}
    #     counter = 0

    #     for num in nums:
    #         diff = target - num
    #         if diff in tracker and tracker[diff] == 0:
    #             counter += 1
    #             tracker[diff] = 1
    #             tracker[num] = 1
    #         if diff not in tracker:
    #             tracker[num] = 0

    #     return counter


    # solution 2: two pointer, should sort first
    def twoSum6(self, nums, target):
        if not nums or len(nums) <= 1:
            return 0

        nums.sort()

        counter = 0
        left, right = 0, len(nums) - 1

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                counter += 1
                left += 1
                right -= 1
                # this comparision is done after update left, right pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1

        return counter









