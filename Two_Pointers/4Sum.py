# Description
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?

# Find all unique quadruplets in the array which gives the sum of target.

# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.

# Example
# Example 1:

# Input:

# numbers = [2,7,11,15]
# target = 3
# Output:

# []
# Explanation:

# 2 + 7 + 11 + 15 != 3. There is no quadruple satisfying the condition.
# Example 2:

# Input:

# numbers = [1,0,-1,0,-2,2]
# target = 0
# Output:

# [[-1, 0, 0, 1],[-2, -1, 1, 2],[-2, 0, 0, 2]]
# Explanation:

# There are three different quadruples whose sum of four numbers is 0.


class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        if not numbers:
            return []

        result =[]
        numbers.sort()

        for a in range(len(numbers)-3):
            if a > 0 and numbers[a] == numbers[a-1]:
                continue
            for b in range(a+1, len(numbers)-2):
                if b > a+1 and numbers[b] == numbers[b-1]:
                    continue

                left = b+1
                right = len(numbers)-1
                value = target - numbers[a] - numbers[b]
                self.find_two_sum(numbers, a, b, left, right, value, result)
                # while left < right:
                #     two_sum = numbers[left] + numbers[right]
                #     if two_sum == value:
                #         result.append([numbers[a], numbers[b], numbers[left], numbers[right]])
                #         left += 1
                #         right -= 1
                #         while left < right and numbers[left] == numbers[left-1]:
                #             left += 1
                #         while left < right and numbers[right] == numbers[right+1]:
                #             right -= 1
                #     elif two_sum > value:
                #         right -= 1
                #     else:
                #         left += 1

        return result


    def find_two_sum(self, numbers, a, b, left, right, value, result):
         while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == value:
                result.append([numbers[a], numbers[b], numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left-1]:
                    left += 1
                while left < right and numbers[right] == numbers[right+1]:
                    right -= 1
            elif two_sum > value:
                right -= 1
            else:
                left += 1













