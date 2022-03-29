# Description
# Given an unsorted array num of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n)O(n) complexity.
# len(num) <= 10000len(num)<=10000
# Example
# Example 1:

# Input:

# num = [100, 4, 200, 1, 3, 2]
# Output:

# 4
# Explanation:

# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:4

from typing import (
    List,
)

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longest_consecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = float('-inf')

        for num in numSet:
            # check if the num is the start a sequence
            length = 1
            if num - 1 not in numSet:
                # need to use num + length since we are updating length each time
                while num + length in numSet:
                    length += 1

            longest = max(longest, length)

        return longest

        # similiar approach
        # numSet = set(nums)
        # longest = -float('inf')

        # for num in nums:
        #     down = num - 1
        #     while down in numSet:
        #         numSet.discard(down)
        #         down -= 1

        #     up = num + 1
        #     while up in numSet:
        #         numSet.discard(up)
        #         up += 1

        #     longest = max(longest, up - down - 1)

        # return longest




