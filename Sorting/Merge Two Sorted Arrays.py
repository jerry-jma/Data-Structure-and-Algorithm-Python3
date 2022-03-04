# Description
# Merge two given sorted ascending integer array A and B into a new sorted integer array.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Example
# Example 1:

# Input:

# A = [1]
# B = [1]
# Output:

# [1,1]
# Explanation:

# return array merged.

# Example 2:

# Input:

# A = [1,2,3,4]
# B = [2,4,5,6]
# Output:

# [1,2,2,3,4,4,5,6]
# Challenge
# How can you optimize your algorithm if one array is very large and the other is very small?

from typing import (
    List,
)

class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        i, j = 0, 0
        result = []

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        while i < len(a):
            result.append(a[i])
            i += 1

        while j < len(b):
            result.append(b[j])
            j += 1

        return result