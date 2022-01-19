# Description
# Given an integer array, sort it in ascending order in place. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

# Wechat reply the 【464】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example1:

# Input: [3, 2, 1, 4, 5],
# Output: [1, 2, 3, 4, 5].
# Example2:

# Input: [2, 3, 1],
# Output: [1, 2, 3].

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    # Solution 1: quick sort, Time O(N*LogN), Space o(N)
    # def sortIntegers2(self, A):
    #     # write your code here
    #     if not A or len(A) == 0:
    #         return -1
    #     self.quick_sort(A, 0, len(A) - 1)

    # def quick_sort(self, A, start, end):
    #     if start >= end:
    #         return

    #     left, right = start, end
    #     pivot = A[(start + end) // 2]

    #     while left <= right:
    #         while left <= right and A[left] < pivot:
    #             left += 1
    #         while left <= right and A[right] > pivot:
    #             right -= 1
    #         if left <= right:
    #             A[left], A[right] = A[right], A[left]
    #             left += 1
    #             right -= 1

    #     self.quick_sort(A, start, right)
    #     self.quick_sort(A, left, end)

    # solution 2: Merge sort, time O(N*logN), space O(N)
    def sortIntegers2(self, A):
        if not A or len(A) == 0:
            return
        temp = [0 for _ in range(len(A))]
        self.merge_sort(A, temp, 0, len(A) - 1)

    def merge_sort(self, A, temp, start, end):
        if start >= end:
            return

        middle = start + (end - start) // 2

        self.merge_sort(A, temp, start, middle)
        self.merge_sort(A, temp, middle + 1, end)

        self.merge(A, temp, start, middle, end)

    def merge(self, A, temp, start, middle, end):
        left_index = start
        right_index = middle + 1
        index = start

        while left_index <= middle and right_index <= end:
            if A[left_index] < A[right_index]:
                temp[index] = A[left_index]
                index += 1
                left_index += 1
            else:
                temp[index] = A[right_index]
                index += 1
                right_index += 1

        while left_index <= middle:
            temp[index] = A[left_index]
            index += 1
            left_index += 1

        while right_index <= end:
            temp[index] = A[right_index]
            index += 1
            right_index += 1
        print(start, end)
        for i in range(start, end + 1):
            A[i] = temp[i]












