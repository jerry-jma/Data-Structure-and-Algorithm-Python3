# Description
# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

# Wechat reply 【56】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# You may assume that each input would have exactly one solution

# Example
# Example 1:

# Input:

# numbers = [2,7,11,15]
# target = 9
# Output:

# [0,1]
# Explanation:

# numbers[0] + numbers[1] = 9

# Example 2:

# Input:

# numbers = [15,2,7,11]
# target = 9
# Output:

# [1,2]
# Explanation:

# numbers[1] + numbers[2] = 9

# Challenge
# Either of the following solutions are acceptable:

# O(n) Space, O(nlogn) Time
# O(n) Space, O(n) Time

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    # Solution 1: use hashmap
    # def twoSum(self, numbers, target):
    #     if not numbers or len(numbers) <= 1:
    #         return

    #     tracker = {}

    #     for idx,num in enumerate(numbers):
    #         diff = target - num
    #         if diff in tracker:
    #             return [tracker[diff], idx]
    #         tracker[num] = idx

    #     return


    # solution 2: Use two pointers after sorted
    def twoSum(self, numbers, target):
        if not numbers or len(numbers) == 0:
            return [-1, -1]

        nums = [
            (number, idx)
            for idx, number in enumerate(numbers)
        ]

        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left][0] + nums[right][0] > target:
                right -= 1
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                return sorted([nums[left][1], nums[right][1]])

        return [-1, -1]









