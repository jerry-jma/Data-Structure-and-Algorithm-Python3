# Description
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Wechat reply the 【148】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# You are not suppose to use the library's sort function for this problem.
# You should do it in-place (sort numbers in the original array).
# You are not allowed to use counting sort to solve this problem.

# Example
# Example 1

# Input : [1, 0, 1, 2]
# Output : [0, 1, 1, 2]
# Explanation : sort it in-place
# Challenge
# Could you come up with an one-pass algorithm using only O(1) space?

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    # solution 1: counter color, time: O(N)
    # def sortColors(self, nums):
    #     if not nums or len(nums) == 0:
    #         return -1

    #     color_counter = [0] * 3
    #     for num in nums:
    #         color_counter[num] += 1

    #     index = 0
    #     for idx in range(len(color_counter)):
    #         number_of_color = color_counter[idx]
    #         for _ in range(number_of_color):
    #             nums[index] = idx
    #             index += 1

    # # solution #2: quick sort partition time: O(n)
    # def sortColors(self, nums):
    #     if not nums or len(nums) == 0:
    #         return -1
    #     self.quick_sort_helper(nums,1)
    #     self.quick_sort_helper(nums,2)

    # def quick_sort_helper(self, nums, partition):
    #     wall = 0
    #     for idx in range(len(nums)):
    #         if nums[idx] < partition:
    #             nums[wall], nums[idx] = nums[idx], nums[wall]
    #             wall += 1

    #  solution #3: 3 pointers, time O(n), space O(1)
    def sortColors(self, nums):
        if not nums or len(nums) == 0:
            return -1

        left, index, right = 0, 0, len(nums) - 1
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1