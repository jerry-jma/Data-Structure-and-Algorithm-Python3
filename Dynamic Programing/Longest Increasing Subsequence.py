# Description
# Given a sequence of integers, find the longest increasing subsequence (LIS).

# You code should return the length of the LIS.

# Wechat reply the 【76】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# What's the definition of longest increasing subsequence?

# The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

# https://en.wikipedia.org/wiki/Longest_increasing_subsequence

# Example
# Example 1:

# Input:

# nums = [5,4,1,2,3]
# Output:

# 3
# Explanation:

# LIS is [1,2,3]
# Example 2:

# Input:

# nums = [4,2,4,5,3,7]
# Output:

# 4
# Explanation:

# LIS is [2,4,5,7]

# Challenge
# Time complexity O(n^2)O(n
# 2
#  ) or O(nlogn)O(nlogn)

from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        pre = [-1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
                    pre[i] = j

        longest, last = 0, -1

        for k in range(len(dp)):
            if dp[k] > longest:
                longest = dp[k]
                last = k

        path = []

        while last != -1:
            print('wat', nums[last], last)
            path.append(nums[last])
            last = pre[last]

        print(path[::-1])

        return longest
