# Description
# Given some points and an origin in two-dimensional space,Find k points from points which are closest to origin Euclidean.Return to the answer from small to large according to Euclidean distance. If two points have the same Euclidean distance, they are sorted by x values. If the x value is the same, then we sort it by the y value.

# Wechat reply question number to get job skills free video package. (wechat id : jiuzhang15)

# Example
# Example 1:

# Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
# Output: [[1,1],[2,5],[4,4]]
# Example 2:

# Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
# Output: [[0,0]]
# Challenge
# O(nlogn) is OK, but can you think of a solution to O(nlogk)？

from typing import (
    List,
)
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""
# solution 1: using Min Heap, pretty slow
import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    # def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
    #     heap = []

    #     for point in points:
    #         distance = self.get_distance(point, origin)
    #         heapq.heappush(heap, (distance, point.x, point.y))

    #     result = []
    #     print('what is heap', heap)
    #     for _ in range(k):
    #         _, x, y = heapq.heappop(heap)
    #         result.append(Point(x, y))

    #     return result

    # def get_distance(self, a, b):
    #     return (a.x - b.x)**2 + (a.y - b.y)**2

    # solution 2: python onlys has min heap, but can be used as MAX Heap
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        heap = []

        for point in points:
            distance = self.get_distance(point, origin)
            heapq.heappush(heap, (-distance, -point.x, -point.y))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while len(heap) > 0:
            _, x, y = heapq.heappop(heap)
            result.append((-x, -y))

        result.reverse()
        return result

    def get_distance(self, a, b):
        return (a.x - b.x)**2 + (a.y - b.y)**2










