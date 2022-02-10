# Description
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Wechat reply the 【900】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example
# Example1

# Input: root = {5,4,9,2,#,8,10} and target = 6.124780
# Output: 5
# Explanation：
# Binary tree {5,4,9,2,#,8,10},  denote the following structure:
#         5
#        / \
#      4    9
#     /    / \
#    2    8  10
# Example2

# Input: root = {3,2,4,1} and target = 4.142857
# Output: 4
# Explanation：
# Binary tree {3,2,4,1},  denote the following structure:
#      3
#     / \
#   2    4
#  /
# 1

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    # solution 1: non-recursive
    def closestValue(self, root, target):
        upper = root
        lower = root

        while root:
            if root.val < target:
                lower = root
                root = root.right
            elif root.val > target:
                upper = root
                root = root.left
            else:
                return root.val
        # abs is a must, see {3,2,4,1} 4.14 example
        if abs(upper.val - target) <= abs(target - lower.val):
            return upper.val

        return lower.val

        # solution 2: recursive






