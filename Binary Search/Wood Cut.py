# Description
# Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

# The unit of length is centimeter.The length of the woods are all positive integers,you couldn't cut wood into float length.If you couldn't get >= k pieces, return 0.

# Example
# Example 1

# Input:
# L = [232, 124, 456]
# k = 7
# Output: 114
# Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
# Example 2

# Input:
# L = [1, 2, 3]
# k = 7
# Output: 0
# Explanation: It is obvious we can't make it.
# Challenge
# O(n log Len), where Len is the longest length of the wood.


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if not L:
            return 0

        start = 1
        # end = min(max(L), sum(L)//k)
        # if end < 1:
        #     return 0

        end = max(L) #use this, return 0 at the end

        while start + 1 < end:
            mid = (start+end) // 2
            if self.getPieces(L, mid) >= k:
                start = mid
            else:
                end = mid
        # should check end matches first because end is longer
        if self.getPieces(L, end) >= k:
            return end
        if self.getPieces(L, start) >= k:
            return start

        return 0

    def getPieces(self, L, length):
        total = 0
        for wood in L:
            total += wood // length
        return total
