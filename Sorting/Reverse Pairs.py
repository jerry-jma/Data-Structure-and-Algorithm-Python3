# Description
# Two numbers in the array, if the previous number is greater than the following number, then the two numbers form a reverse order pair. Give you an array, find out the total number of reverse order pairs in this array.
# Summary: if a [i] > a [j] and i < j, a [i] and a [j] form a reverse order pair.

# Wechat reply the 【532】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example1

# Input:  A = [2, 4, 1, 3, 5]
# Output: 3
# Explanation:
# (2, 1), (4, 1), (4, 3) are reverse pairs
# Example2

# Input:  A = [1, 2, 3, 4]
# Output: 0
# Explanation:
# No reverse pair

class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        length = len(A)
        if not A or length == 0:
            return 0
        temp = [0] * length
        return self.merge_sort(A, temp, 0, length - 1)

    def merge_sort(self, A, temp, start, end):
        if start >= end:
            return 0

        counter = 0
        mid = start + (end - start) // 2
        counter += self.merge_sort(A, temp, start, mid)
        counter += self.merge_sort(A, temp, mid + 1, end)
        counter += self.merge(A, temp, start, mid, end)
        return counter

    def merge(self, A, temp, start, mid, end):
        if start >= end:
            return 0

        left_index = start
        right_index = mid + 1
        temp_index = start
        temp_counter = 0
        while left_index <= mid and right_index <= end:
            if A[left_index] <= A[right_index]:
                temp[temp_index] = A[left_index]
                left_index += 1
            else:
                temp_counter += mid - left_index + 1
                temp[temp_index] = A[right_index]
                right_index += 1

            temp_index += 1

        while left_index <= mid:
            temp[temp_index] = A[left_index]
            temp_index += 1
            left_index += 1

        while right_index <= end:
            temp[temp_index] = A[right_index]
            temp_index += 1
            right_index += 1

        for i in range(start, end + 1):
            A[i] = temp[i]

        return temp_counter
