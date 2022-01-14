# Description
# Given an array arr and a nonnegative integer k, you need to find a continuous array from this array so that the sum of this array is k. Output the length of this array. If there are multiple such substrings, return the one with the minimum ending position; if there are multiple answers, return the one with the minimum starting position. If no such subarray is found, -1 is returned.

# The length of the array does not exceed 10^610
# 6
#  , each number in the array is less than or equal to 10^610
# 6
#  , and k does not exceed 10^610
# 6
#  .

# Example
# Example 1 :

# Input：arr=[1,2,3,4,5] ，k=5
# Output：2
# Explanation:
# In this array, the earliest contiguous substring is [2,3].
# Example 2 :

# Input：arr=[3,5,7,10,2] ，k=12
# Output：2
# Explanation:
# In this array, the earliest consecutive concatenated substrings with a sum of 12 are [5,7].

class Solution:
    def searchSubarray(self, arr, k):
        prefix_sum_n_idx = {0: 1}
        prefix_sum = 0

        for idx, val in enumerate(arr):
            prefix_sum += val
            prev_sum = prefix_sum - k

            if prev_sum in prefix_sum_n_idx:
                return i - prefix_sum_n_idx[prev_sum]
            if prefix_sum not in prefix_sum_n_idx:
                prefix_sum_n_idx[prefix_sum] = idx

        return -1