# Description
# Merge two sorted (ascending) lists of interval and return it as a new sorted list. The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# The intervals in the given list do not overlap.
# The intervals in different lists may overlap.
# Example
# Example1

# Input: list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)]
# Output: [(1,4),(5,6)]
# Explanation:
# (1,2),(2,3),(3,4) --> (1,4)
# (5,6) --> (5,6)
# Example2

# Input: list1 = [(1,2),(3,4)] and list2 = [(4,5),(6,7)]
# Output: [(1,2),(3,5),(6,7)]
# Explanation:
# (1,2) --> (1,2)
# (3,4),(4,5) --> (3,5)
# (6,7) --> (6,7)

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def merge_two_interval(self, list1: List[Interval], list2: List[Interval]) -> List[Interval]:
        intervals = list1 + list2

        if not intervals:
            return []

        result = []
        prev = None

        intervals = sorted(intervals, key=lambda interval:interval.start)

        for interval in intervals:
            if not prev or interval.start > prev.end:
                result.append(interval)
                prev = result[-1]
            else:
                prev.end = max(prev.end, interval.end)

        return result


