# Description
# Given a set of candidate numbers candidates and a target number target. Find all unique combinations in candidates where the numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Wechat reply the 【135】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# All numbers (including target) will be positive integers.
# Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
# Different combinations can be in any order.
# The solution set must not contain duplicate combinations.
# Example
# Example 1:

# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[7], [2, 2, 3]]
# Example 2:

# Input: candidates = [1], target = 3
# Output: [[1, 1, 1]]

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # all positive
        # non-descending, it's sorted
        # same number can be used many times
        # no duplicate combination
        if not candidates:
            return []

        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, 0, target, [], results)
        return results

    def dfs(self, candidates, index, target, curr_result, results):
        if target == 0:
            results.append(list(curr_result))

        for i in range(index, len(candidates)):
            if target < candidates[i]:
                return

            curr_result.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], curr_result, results)
            curr_result.pop()


