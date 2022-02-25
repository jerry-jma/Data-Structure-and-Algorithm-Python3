# Description
# Given two numbers, number a and number b. Find the greatest common divisor of the given two numbers.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# In mathematics, the greatest common divisor (gcd) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers.

# Example
# Example1

# Input: a = 10, b = 15
# Output: 5
# Explanation:
# 10 % 5 == 0
# 15 % 5 == 0
# Example2

# Input: a = 15, b = 30
# Output: 15
# Explanation:
# 15 % 15 == 0
# 30 % 15 == 0

class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a: int, b: int) -> int:
        # if a == 0 or b == 0:
        #     return a + b

        if a < b:
            a, b = b, a

        if a % b != 0:
            return self.gcd(b, a%b)
        else:
            return b
