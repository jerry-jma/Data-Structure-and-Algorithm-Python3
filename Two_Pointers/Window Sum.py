# Description
# Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Example
# Example 1

# Input：array = [1,2,7,8,5], k = 3
# Output：[10,17,20]
# Explanation：
# 1 + 2 + 7 = 10
# 2 + 7 + 8 = 17
# 7 + 8 + 5 = 20


from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def win_sum(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k < 0 or len(nums) < k:
            return []

        result = []
        fast = 0
        window_sum = 0

        for slow in range(len(nums)):
            while fast < len(nums) and fast - slow < k:
                window_sum += nums[fast]
                fast += 1
            if fast - slow == k:
                result.append(window_sum)
            window_sum -= nums[slow]

        return result