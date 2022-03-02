# Description
# Given k sorted integer arrays, merge them into one sorted array.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Example
# Example 1:

# Input:
#   [
#     [1, 3, 5, 7],
#     [2, 4, 6],
#     [0, 8, 9, 10, 11]
#   ]
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Example 2:

# Input:
#   [
#     [1,2,3],
#     [1,2]
#   ]
# Output: [1,1,2,2,3]
# Challenge
# Do it in O(N log k).

# N is the total number of integers.
# k is the number of arrays.

from typing import (
    List,
)

import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    # Solution 1: Using heap
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        if not arrays:
            return []

        result = []
        heap = []

        for i, arr in enumerate(arrays):
            if len(arr) > 0:
                heapq.heappush(heap, (arr[0], i, 0))

        while heap:
            val, idx, curr_idx = heapq.heappop(heap)
            result.append(val)

            if curr_idx + 1 < len(arrays[idx]):
                heapq.heappush(heap, (arrays[idx][curr_idx+1], idx, curr_idx+1))

        return result