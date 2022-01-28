# Description
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Wechat reply question number 69 to get Universal algorithm template . (wechat id : jiuzhang15)

# The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
# The number of nodes does not exceed 20.
# Example
# Example 1:

# Input:

# tree = {1,2,3}
# Output:

# [[1],[2,3]]
# Explanation:

#    1
#   / \
#  2   3
# it will be serialized {1,2,3}
# Example 2:

# Input:

# tree = {1,#,2,3}
# Output:

# [[1],[2],[3]]
# Explanation:

# 1
#  \
#   2
#  /
# 3
# it will be serialized {1,#,2,3}

# Challenge
# Challenge 1: Using only 1 queue to implement it.

# Challenge 2: Use BFS algorithm to do it.


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    # def levelOrder(self, root):
    #     # write your code here
    #     if not root:
    #         return []

    #     results = []
    #     queue = collections.deque([root])

    #     while queue:
    #         level = []
    #         length = len(queue)

    #         for _ in range(length):
    #             curr_node = queue.popleft()
    #             level.append(curr_node.val)
    #             if curr_node.left:
    #                 queue.append(curr_node.left)
    #             if curr_node.right:
    #                 queue.append(curr_node.right)
    #         results.append(level)

    #     return results