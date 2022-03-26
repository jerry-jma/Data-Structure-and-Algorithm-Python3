# Description
# Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

# You are not necessary to keep the original order of positive integers or negative integers.

# Example
# Example 1

# Input : [-1, -2, -3, 4, 5, 6]
# Outout : [-1, 5, -2, 4, -3, 6]
# Explanation :  any other reasonable answer.
# Challenge
# Do it in-place and without extra memory.

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        if not A:
            return
        neg_count = self.partition(A)
        pos_count = len(A) - neg_count
        # draw out all three cases
        # left = 1 if neg_count > pos_count else 0
        # right = len(A) - (1 if neg_count >= pos_count else 2)

        if neg_count > pos_count:
            left, right = 1, len(A) - 1
        elif neg_count < pos_count:
            left, right = 0, len(A) - 2
        else:
            left, right = 0, len(A) - 1

        self.interleave(A, left, right)

    def partition(self, A):
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] < 0:
                left += 1
            while left <= right and A[right] > 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        return left

    def interleave(self, A, left, right):
        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 2
            right -= 2
