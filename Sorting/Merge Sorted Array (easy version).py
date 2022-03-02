# Description
# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

# Example
# Example 1:

# Input:

# A = [1,2,3]
# m = 3
# B = [4,5]
# n = 2
# Output:

# [1,2,3,4,5]
# Explanation:

# After merge, A will be filled as [1,2,3,4,5]
# Example 2:

# Input:

# A = [1,2,5]
# m = 3
# B = [3,4]
# n = 2
# Output:

# [1,2,3,4,5]
# Explanation:

# After merge, A will be filled as [1,2,3,4,5]

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        i, j = 0, 0
        arr = []

        while i < m and j < n:
            if A[i] < B[j]:
                arr.append(A[i])
                i += 1
            else:
                arr.append(B[j])
                j += 1

        while i < m:
            arr.append(A[i])
            i += 1

        while j < n:
            arr.append(B[j])
            j += 1

        for i in range(len(A)):
            A[i] = arr[i]
