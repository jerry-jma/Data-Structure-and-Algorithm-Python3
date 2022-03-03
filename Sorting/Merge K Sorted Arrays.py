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

   # Solution 2: Using Merge Sort
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        if not arrays:
            return []

        return self.mergeAll(arrays, 0, len(arrays) - 1)

    def mergeAll(self, arrays, start, end):
        if start == end:
            return arrays[start]

        mid = (start + end) // 2
        left = self.mergeAll(arrays, start, mid)
        right = self.mergeAll(arrays, mid + 1, end)
        return self.mergeTwo(left, right)

    def mergeTwo(self, arr1, arr2):
        i, j = 0, 0
        result = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result

   # Solution 3: merge two at a time
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        if not arrays:
            return []

        while len(arrays) > 1:
            new_arrays = []

            for i in range(0, len(arrays), 2):
                if i + 1 < len(arrays):
                    new_list = self.mergeTwo(arrays[i], arrays[i+1])
                else:
                    new_list = arrays[i]
                new_arrays.append(new_list)

            arrays = new_arrays

        return arrays[0]


    def mergeTwo(self, arr1, arr2):
        i, j = 0, 0
        result = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result