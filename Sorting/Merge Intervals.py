# Description
# Given a collection of intervals, merge all overlapping intervals.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Example
# Example 1:

# Input: [(1,3)]
# Output: [(1,3)]
# Example 2:

# Input:  [(1,3),(2,6),(8,10),(15,18)]
# Output: [(1,6),(8,10),(15,18)]
# Challenge
# O(n log n) time and O(1) extra space.

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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return []

        result = []
        prev = None

        intervals = sorted(intervals, key=lambda interval:interval.start)

        for interval in intervals:
            if not prev or interval.start > prev.end:
                result.append(interval)
                prev = interval
            else:
                prev.end = max(prev.end, interval.end)

        return result
