# Description
# Given a set with distinct integers, return all possible subsets.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Example
# Example 1:

# Input:

# nums = [0]
# Output:

# [
#   [],
#   [0]
# ]
# Explanation:

# The subsets of [0] are only [] and [0].

# Example 2:

# Input:

# nums = [1,2,3]
# Output:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# Explanation:

# The subsets of [1,2,3] are [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].

# Challenge
# Can you do it in both recursively and non-recursively?

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
       nums = sorted(nums)
       combinations = []
       self.dfs(nums, 0, [], combinations)
       return combinations

    def dfs(self, nums, index, combination, combinations):
        # or use list(combination) to create a new copy
        combinations.append(combination[:])

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i+1, combination, combinations)
            combination.pop()

    # solution 2: BFS
    # def subsets(self, nums):
    #     if not nums:
    #         return [[]]

    #     queue = [[]]
    #     index = 0

    #     while index < len(queue):
    #         subset = queue[index]
    #         for num in nums:
    #             if subset and subset[-1] >= num:
    #                 continue
    #             queue.append(subset + [num])
    #         index += 1

    #     return queue