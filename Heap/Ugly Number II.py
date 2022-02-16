# Description
# Ugly number is a number that only have prime factors 2, 3 and 5.

# Design an algorithm to find the Nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

# Note that 1 is typically treated as an ugly number.

# Wechat reply the 【4】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# 1 \leq n \leq 10^{5}1≤n≤10
# 5


# Example
# Example 1:

# Input:

# n = 9
# Output:

# 10
# Explanation:

# [1,2,3,4,5,6,8,9,10,....],the ninth ugly number is 10.

# Example 2:

# Input:

# n = 1
# Output:

# 1
# Challenge
# O(n log n) or O(n) time.

import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    # def nthUglyNumber(self, n):
    #     heap = [1]
    #     seen = set([1])
    #     curr_ugly = 1

    #     for _ in range(n):
    #         curr_ugly = heapq.heappop(heap)
    #         for factor in [2,3,5]:
    #             new_ugly = curr_ugly * factor
    #             if new_ugly not in seen:
    #                 seen.add(new_ugly)
    #                 heapq.heappush(heap, new_ugly)

    #     return curr_ugly

    # solution 2: Using DP
    def nthUglyNumber(self, n):
        dp = [0] * n
        dp[0] = 1
        l2, l3, l5 = 0, 0, 0

        for i in range(1, n):
            dp[i] = min(2*dp[l2], 3*dp[l3], 5*dp[l5])
            if dp[i] == 2 * dp[l2]:
                l2 += 1
            if dp[i] == 3 * dp[l3]:
                l3 += 1
            if dp[i] == 5 * dp[l5]:
                l5 += 1

        return dp[-1]
