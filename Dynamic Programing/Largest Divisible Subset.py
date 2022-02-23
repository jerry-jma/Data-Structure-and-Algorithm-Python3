# Description
# Given a set of distinct positive integers, find the largest subset which has the most elements, and every pair of two elements (Si, Sj) in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# If there are multiple solutions, return any subset is fine.
# 1 \leq len(nums) \leq 500001≤len(nums)≤50000

# Example
# Example 1:

# Input: nums =  [1,2,3],
# Output: [1,2] or [1,3]
# Example 2:

# Input: nums = [1,2,4,8],
# Output: [1,2,4,8]

class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums = sorted(nums)
        length = len(nums)

        dp = {}
        pre = {}

        for num in nums:
            dp[num] = 1
            pre[num] = -1

        last_num = nums[0]
        for num in nums:
            for factor in self.get_factors(num):
                if factor not in dp:
                    continue
                if dp[num] < dp[factor] + 1:
                    dp[num] = dp[factor] + 1
                    pre[num] = factor
            if dp[num] > dp[last_num]:
                last_num = num

        return self.get_path(pre, last_num)

    def get_factors(self, num):
        if num == 1:
            return []

        factor = 1
        factors = []

        while factor * factor <= num:
            if num % factor == 0:
                factors.append(factor)
                if factor * factor != num and factor != 1:
                    factors.append(num // factor)
            factor += 1

        return factors

    def get_path(self, pre, last_num):
        path = []

        while last_num != -1:
            path.append(last_num)
            last_num = pre[last_num]

        return path[::-1]