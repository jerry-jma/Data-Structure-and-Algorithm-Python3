# Description
# Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# Wechat reply 【159】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# You can assume no duplicate exists in the array.

# Example
# Example 1:

# Input：[4, 5, 6, 7, 0, 1, 2]
# Output：0
# Explanation：
# The minimum value in an array is 0.
# Example 2:

# Input：[2,1]
# Output：1
# Explanation：
# The minimum value in an array is 1.

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            # if it's all sorted and not rotated
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + end) // 2
            # whiteboard this part is easier to understand
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
        print(start, end)
        return min(nums[start], nums[end])
