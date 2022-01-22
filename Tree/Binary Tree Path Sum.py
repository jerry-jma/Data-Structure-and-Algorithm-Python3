# Description
# Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

# A valid path is from root node to any of the leaf nodes.

# Wechat reply the 【376】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input:
# {1,2,4,2,3}
# 5
# Output: [[1, 2, 2],[1, 4]]
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
# Example 2:

# Input:
# {1,2,4,2,3}
# 3
# Output: []
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# Notice we need to find all paths from root node to leaf nodes.
# 1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5
# There is no one satisfying it.

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
       if not root:
            return []

        result = []
        path = []
        self.helper(root, target, path, result)
        return result

    def helper(self, node, target, path, result):
        if not node.left and not node.right:
            if node.val == target:
                result += [path + [node.val]]

        if node.left:
            self.helper(node.left, target - node.val, path + [node.val], result)

        if node.right:
            self.helper(node.right, target - node.val, path + [node.val], result)


    # def binaryTreePathSum(self, root, target):
    #     results = []
    #     path = []
    #     self.dfs(root, results, path, 0, target)
    #     return results

    # def dfs(self, root, results, path, curr_total, target):
    #     if not root:
    #         return

    #     path.append(root.val)
    #     curr_total += root.val

    #     if not root.left and not root.right and curr_total == target:
    #         results.append(path[::1])

    #     self.dfs(root.left, results, path, curr_total, target)
    #     self.dfs(root.right, results, path, curr_total, target)

    #     print('above', curr_total, path, results)
    #     path.pop()
    #     print('below', curr_total, path, results)