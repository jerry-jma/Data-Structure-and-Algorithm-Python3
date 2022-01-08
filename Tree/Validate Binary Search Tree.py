# Description
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# A single node tree is a BST
# Wechat reply question number to get job skills free video package. (wechat id : jiuzhang15)

# Example
# Example 1:

# Input:

# tree = {-1}
# Output:

# true
# Explanation:

# For the following binary tree（only one node）:
#               -1
# This is a binary search tree.
# Example 2:

# Input:

# tree = {2,1,4,#,#,3,5}
# Output:

# true
# Explanation:

# For the following binary tree:
#           2
#          / \
#         1   4
#            / \
#           3   5
# This is a binary search tree.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, left_min, right_max):
        if not node:
            return True
        if not (node.val < right_max and node.val > left_min):
            return False

        return self.valid(node.left, left_min, node.val)\
            and self.valid(node.right, node.val, right_max)