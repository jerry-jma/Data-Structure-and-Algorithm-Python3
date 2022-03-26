`# Description
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.

# Example
# Example 1:

# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]

# Output:
# 2

# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
# Example 2:

# Input:
# A = [0]
# B = [0]
# C = [0]
# D = [0]

# Output:
# 1


from typing import (
    List,
)

class Solution:
    """
    @param a: a list
    @param b: a list
    @param c: a list
    @param d: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def four_sum_count(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        tracker = {}

        for a_val in a:
            for b_val in b:
                total = a_val + b_val
                tracker[total] = tracker.get(total, 0) + 1

        counter = 0

        for c_val in c:
            for d_val in d:
                total = c_val + d_val
                counter += tracker.get(-total, 0)

        return counter