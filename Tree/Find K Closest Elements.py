# Description
# Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

# Contact me on wechat to get more FLAMG requent Interview questions . (wechat id : jiuzhang15)

# The value k is a non-negative integer and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 10^410
# 4

# Absolute value of elements in the array will not exceed 10^410
# 4

# Example
# Example 1:

# Input: A = [1, 2, 3], target = 2, k = 3
# Output: [2, 1, 3]
# Example 2:

# Input: A = [1, 4, 6, 8], target = 3, k = 3
# Output: [4, 1, 6]
# Challenge
# O(logn + k) time

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        if not A:
            return []
        result = []
        index = self.findPosition(A, target)
        left = index - 1
        right = index

        for _ in range(k):
            if left < 0:
                result.append(A[right])
                right += 1
            elif right == len(A):
                result.append(A[left])
                left -= 1
            else:
                if target - A[left] <= A[right] - target:
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1

        return result

    def findPosition(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if target > A[mid]:
                start = mid
            elif target < A[mid]:
                end = mid
            else:
                return mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end

        return len(A)

