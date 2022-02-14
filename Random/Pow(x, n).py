# Description
# Implement pow(x, n). (n is an integer.)

# Wechat reply the 【428】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

# Example
# Example 1:

# Input: x = 9.88023, n = 3
# Output: 964.498
# Example 2:

# Input: x = 2.1, n = 3
# Output: 9.261
# Example 3:

# Input: x = 1, n = 0
# Output: 1
# Challenge
# O(logn) time

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if x == 0:
            return 0
        result = self.helper(x, abs(n))
        return result if n > 0 else 1 / result

    def helper(self, x, n):
        if n == 0:
            return 1

        temp = self.helper(x, n // 2)
        res = temp * temp

        return res * x if n % 2 == 1 else res