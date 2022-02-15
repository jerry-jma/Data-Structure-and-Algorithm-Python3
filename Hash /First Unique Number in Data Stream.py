# Description
# Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the terminating number is not found, return -1.

# Wechat reply the 【685】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example1

# Input:
# [1, 2, 2, 1, 3, 4, 4, 5, 6]
# 5
# Output: 3
# Example2

# Input:
# [1, 2, 2, 1, 3, 4, 4, 5, 6]
# 7
# Output: -1
# Example3

# Input:
# [1, 2, 2, 1, 3, 4]
# 3
# Output: 3
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # 1,2,2,1,3,4,4,5
        #         3     5
        tracker = {}
        for num in nums:
            tracker[num] = tracker.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1

        for num in nums:
            if tracker[num] == 1:
                return num
