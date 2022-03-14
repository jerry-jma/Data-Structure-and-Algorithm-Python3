# Description
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Trapping Rain Water

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)


# Example
# Example 1:

# Input: [0,1,0]
# Output: 0
# Example 2:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Challenge
# O(n) time and O(1) memory

# O(n) time and O(n) memory is also acceptable.

from typing import (
    List,
)

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    # Solution 1: min(左侧最高，右侧最高) - 当前高度
    # 时间复杂度O(n)，空间复杂度O(n)
    def trap_rain_water(self, heights: List[int]) -> int:
        if not heights:
            return 0

        left_max = []
        currMax = -float('inf')

        for height in heights:
            currMax = max(currMax, height)
            left_max.append(currMax)

        right_max = []
        currMax = -float('inf')
        for height in reversed(heights):
            currMax = max(currMax, height)
            right_max.append(currMax)

        right_max = right_max[::-1]

        total = 0
        for i in range(len(heights)):
            total += min(left_max[i], right_max[i]) - heights[i]

        return total









