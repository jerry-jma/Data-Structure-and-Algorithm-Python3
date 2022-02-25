# Description
# Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

# These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

# They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

# Return the shortest time that the slowest copier spends.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# The sum of book pages is less than or equal to 2147483647

# Example
# Example 1:

# Input: pages = [3, 2, 4], k = 2
# Output: 5
# Explanation:
#     First person spends 5 minutes to copy book 1 and book 2.
#     Second person spends 4 minutes to copy book 3.
# Example 2:

# Input: pages = [3, 2, 4], k = 3
# Output: 4
# Explanation: Each person copies one of the books.
# Challenge
# O(nk) time

from typing import (
    List,
)

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, pages: List[int], k: int) -> int:
        if not pages:
            return 0

        start = max(pages)
        end = sum(pages)

        while start + 1 < end:
            mid = (start + end) // 2
            # if the return value is less than k people\
            # meaning we can do better, decrease the time a bit
            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid

        if self.get_least_people(pages, start) <= k:
            return start
        return end

    def get_least_people(self, pages, time_limit):
        people = 0
        time_cost_now = 0

        for page in pages:
            if page + time_cost_now > time_limit:
                people += 1
                time_cost_now= 0
            time_cost_now += page

        return people + 1
