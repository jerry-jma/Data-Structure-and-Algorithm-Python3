# Description
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Contact me on wechat to get more FLAMG requent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input:

# tree = {1,2,3}
# Output:

# true
# Explanation:

# This is a balanced binary tree.
#           1
#          / \
#         2   3
# Example 2:

# Input:

# tree = {1,#,2,3,4}
# Output:

# false
# Explanation:

# This is not a balanced tree.
# The height of node 1's right sub-tree is 2 but left sub-tree is 0.
#            1
#             \
#             2
#            /  \
#           3   4

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
    @return: True if this Binary tree is Balanced, or false.
    """
    # def isBalanced(self, root):
    #     # write your code here
    #     if not root:
    #         return True

    #     if not self.isBalanced(root.left):
    #         return False
    #     if not self.isBalanced(root.right):
    #         return False

    #     return abs(self.get_height(root.left) - self.get_height(root.right)) <= 1

    # def get_height(self, root):
    #     if not root:
    #         return 0

    #     left_depth = self.get_height(root.left) + 1
    #     right_depth = self.get_height(root.right) + 1

    #     return max(left_depth, right_depth)

    def isBalanced(self, root):
        if not root:
             return True

        balanced, height = self.dfs(root)
        print(balanced, height)

        return balanced

    def dfs(self, root):
        if not root:
            return True, 0

        check_left, left_height = self.dfs(root.left)
        check_right, right_height = self.dfs(root.right)

        is_balanced = check_left and check_right and abs(left_height - right_height) <= 1

        return is_balanced, max(left_height, right_height) + 1


















