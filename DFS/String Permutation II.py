# Description
# Given a string, find all permutations of it without duplicates.

# Wechat reply the 【10】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input:

# s = "abb"
# Output:

# ["abb", "bab", "bba"]
# Explanation:

# There are six kinds of full arrangement of abb, among which there are three kinds after removing duplicates.

# Example 2:

# Input:

# s = "aabb"
# Output:

# ["aabb", "abab", "baba", "bbaa", "abba", "baab"]
class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        if str is None:
            return

        array = sorted(list(str))
        permutations = []
        visited = [False] * len(str)

        self.dfs(array, visited, [], permutations)

        return permutations

    def dfs(self, array, visited, permutation, permutations):
        if len(permutation) == len(array):
            permutations.append(''.join(permutation))
            return

        for i in range(len(array)):
            if visited[i]:
                continue
            if i > 0 and array[i-1] == array[i] and not visited[i-1]:
                continue

            visited[i] = True
            permutation.append(array[i])

            self.dfs(array, visited, permutation, permutations)

            permutation.pop()
            visited[i] = False


