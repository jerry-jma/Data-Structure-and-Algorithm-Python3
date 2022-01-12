# Description
# Given an array of integers, remove the duplicate numbers in it.

# You should:

# Do it in place in the array.
# Put the element after removing the repetition at the beginning of the array.
# Return the number of elements after removing duplicate elements.
# You don't need to keep the original order of the integers.

# Example
# Example 1:

# Input:
# nums = [1,3,1,4,4,2]
# Output:
# [1,3,4,2,?,?]
# 4
# Explanation:

# Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
# Return the number of unique integers in nums => 4.
# Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

# Example 2:

# Input:
# nums = [1,2,3]
# Output:
# [1,2,3]
# 3
# Challenge
# Do it in O(n) time complexity.
# Do it in O(nlogn) time without extra space.

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        # nums_holder = set()
        # counter = 0

        # for idx in range(len(nums)):
        #     if nums[idx] not in nums_holder:
        #         nums[counter] = nums[idx]
        #         counter += 1
        #     nums_holder.add(nums[idx])
        # return len(nums_holder)
        # # d, result = {}, 0
        # # for num in nums:
        # #     print(num, nums)
        # #     if num not in d:
        # #         d[num] = True
        # #         nums[result] = num
        # #         result += 1

        # # return result

        length = len(nums)
        if length == 0 or not nums:
            return 0
        if length == 1:
            return 1

        left, right = 0, 1
        nums.sort()

        while right < length:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1

        return left + 1








