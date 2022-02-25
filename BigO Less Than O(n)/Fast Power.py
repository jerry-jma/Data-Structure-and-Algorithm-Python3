# Description
# Calculate the a^n \% ba
# n
#  %b where a, b and n are all 32bit non-negative integers.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# a, b and n are all 32-bit non-negative integers

# Example
# Example 1:

# Input:

# a = 3
# b = 7
# n = 5
# Output:

# 5
# Explanation:

# 3 ^ 5 % 7 = 5

# Example 2:

# Input:

# a = 3
# b = 1
# n = 0
# Output:

# 5
# Explanation:

# 3 ^ 0 % 1 = 0

# Challenge
# O(logn)O(logn) time complexity
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b

        if n == 1:
            return a % b

        power = self.fastPower(a, b, n//2)
        power = power * power % b

        if n % 2 == 1:
            power = (power * a) % b

        return power