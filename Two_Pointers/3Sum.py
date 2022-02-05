# Description
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Wechat reply 【57】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

# The solution set must not contain duplicate triplets.

# Example
# Example 1:

# Input:

# numbers = [2,7,11,15]
# Output:

# []
# Explanation:

# Cannot find triples such that the sum of three numbers is 0.
# Example 2:

# Input:

# numbers = [-1,0,1,2,-1,-4]
# Output:

# [[-1, 0, 1],[-1, -1, 2]]
# Explanation:

# [-1, 0, 1] and [-1, -1, 2] are two triples.1, 2]]


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if not numbers or len(numbers) <= 2:
            return 0

        numbers.sort()
        result = []

        for i in range(len(numbers) - 2):
            curr_num = numbers[i]
            if i > 0 and curr_num == numbers[i - 1]:
                continue
            self.find_two_sum(numbers, -curr_num, i, result)

        return result

    def find_two_sum(self, numbers, target, index, result):
        left = index + 1
        right = len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                result.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1









