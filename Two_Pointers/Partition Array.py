# Description
# Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

# All elements < k are moved to the left
# All elements >= k are moved to the right
# Return the partitioning index, i.e the first index i nums[i] >= k.

# Wechat reply 【31】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

# If all elements in nums are smaller than k, then return nums.length
# 0 <= nums.length <= 20000<=nums.length<=2000

# Example
# Example 1:

# Input:

# nums = []
# k = 9
# Output:

# 0
# Explanation:

# Empty array, print 0.

# Example 2:

# Input:

# nums = [3,2,2,1]
# k = 2
# Output:

# 1
# Explanation:

# the real array is[1,2,2,3].So return 1.

# Challenge
# Can you partition the array in-place and in O(n)O(n)?


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    # solution 1: two pointers, use slow pointer as a wall
    # def partitionArray(self, nums, k):
    #     # write your code here
    #     if not nums or len(nums) == 0:
    #         return 0

    #     slow, fast = 0, 0
    #     is_greater = False
    #     while fast < len(nums):
    #         curr_num = nums[fast]
    #         if curr_num >= k:
    #             fast += 1
    #             is_greater = True
    #         else:
    #             nums[slow], nums[fast] = nums[fast], nums[slow]
    #             slow += 1
    #             fast += 1

    #     if is_greater:
    #         return slow
    #     return len(nums)


    # solution 2: two pointers, one at beginning and one at the end
    def partitionArray(self, nums, k):
        if not nums or len(nums) == 0:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
                # given [3,2,2,1], right will keep going until reach 0
                # so the last if statement will not run after the first swap
            if left <= right:
                print('before', left, right)
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                print(left, right)

        return left









