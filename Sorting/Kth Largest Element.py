# Description
# Find the K-th largest element in an array.

# Wechat reply the 【5】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# You can swap elements in the array.
# 1 \leq k \leq 10^{5}1≤k≤10
# 5


# Example
# Example 1:

# Input:

# k = 1
# nums = [1,3,4,2]
# Output:

# 4
# Explanation:

# The first largest element is four.

# Example 2:

# Input:

# k = 3
# nums = [9,3,2,4,8]
# Output:

# 4
# Explanation:

# The third largest largest element is four.

# Challenge
# O(n) time, O(1) extra memory.


class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    # def kthLargestElement(self, k, nums):
    #     if not nums or k < 1 or k > len(nums):
    #         return None
    #     return self.quick_sort(nums, 0, len(nums) - 1, k)

    # def quick_sort(self, nums, start, end, k):
    #     if start == end:
    #         return nums[start]

    #     left, right = start, end
    #     pivot = nums[(start + end) // 2]

    #     while left <= right:
    #         while left <= right and nums[left] > pivot:
    #             left += 1
    #         while left <= right and nums[right] < pivot:
    #             right -= 1
    #         if left <= right:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1

    #     if k + start - 1 <= right:
    #         return self.quick_sort(nums, start, right, k)
    #     if k + start - 1 >= left:
    #         return self.quick_sort(nums, left, end, k - (left - start))

    #     return nums[right + 1]

    def kthLargestElement(self, k, nums):
        if not nums or k < 1 or k > len(nums):
            return None

        k = len(nums) - k
        return self.quick_select(nums, 0, len(nums) - 1, k)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[k]

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.quick_select(nums, start, right, k)
        if k >= left:
            return self.quick_select(nums, left, end, k)

        return nums[k]
























