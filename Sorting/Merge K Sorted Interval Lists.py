# Merge K sorted interval lists into one sorted interval list. You need to merge overlapping intervals too.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Example
# Example1

# Input: [
#   [(1,3),(4,7),(6,8)],
#   [(1,2),(9,10)]
# ]
# Output: [(1,3),(4,8),(9,10)]
# Example2

# Input: [
#   [(1,2),(5,6)],
#   [(3,4),(7,8)]
# ]
# Output: [(1,2),(3,4),(5,6),(7,8)]

  # Solution 1: merge sort logic
    # def mergeKSortedIntervalLists(self, intervals):
    #     if not intervals:
    #         return []
    #     return self.mergeAll(intervals, 0, len(intervals) - 1)

    # def mergeAll(self, intervals, start, end):
    #     if start == end:
    #         return intervals[start]

    #     mid = (start + end) // 2
    #     left = self.mergeAll(intervals, start, mid)
    #     right = self.mergeAll(intervals, mid + 1, end)
    #     return self.mergeTwo(left, right)

    # def mergeTwo(self, list1, list2):
    #     i, j = 0, 0
    #     result = []

    #     while i < len(list1) and j < len(list2):
    #         if list1[i].start < list2[j].start:
    #             self.mergeNow(list1[i], result)
    #             i += 1
    #         else:
    #             self.mergeNow(list2[j], result)
    #             j += 1

    #     while i < len(list1):
    #         self.mergeNow(list1[i], result)
    #         i += 1

    #     while j < len(list2):
    #         self.mergeNow(list2[j], result)
    #         j += 1

    #     return result

    # def mergeNow(self, interval, result):
    #     if len(result) == 0:
    #         result.append(interval)
    #         return

    #     prev_interval = result[-1]
    #     if interval.start <= prev_interval.end:
    #         prev_interval.end = max(interval.end, prev_interval.end)
    #     else:
    #         result.append(interval)

    # Solution 2: Heap
    def mergeKSortedIntervalLists(self, intervals):
        if not intervals:
            return []

        result = []
        heap = []
        for idx, arr in enumerate(intervals):
            if len(arr) == 0:
                continue
            heapq.heappush(heap, (arr[0].start, arr[0].end, idx, 0))

        while heap:
            start, end, intervals_idx, arr_idx = heapq.heappop(heap)

            self.merge_and_append(result, start, end, intervals, intervals_idx, arr_idx)

            if arr_idx + 1 < len(intervals[intervals_idx]):
                heapq.heappush(heap, (intervals[intervals_idx][arr_idx+1].start, \
                intervals[intervals_idx][arr_idx+1].end, intervals_idx, arr_idx + 1))

        return result

    def merge_and_append(self, result, start, end, intervals, intervals_idx, arr_idx):
        if len(result) == 0:
                result.append(intervals[intervals_idx][arr_idx])

        prev = result[-1]

        if start > result[-1].end:
            result.append(intervals[intervals_idx][arr_idx])
        else:
            prev.end = max(prev.end, end)