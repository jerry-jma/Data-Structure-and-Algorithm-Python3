# Description
# Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
# The range of input and output data is in int.

# Wechat reply the 【596】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

# Example
# Example 1:

# Input:
# {1,-5,2,1,2,-4,-5}
# Output:1
# Explanation:
# The tree is look like this:
#      1
#    /   \
#  -5     2
#  / \   /  \
# 1   2 -4  -5
# The sum of whole tree is minimum, so return the root.
# Example 2:

# Input:
# {1}
# Output:1
# Explanation:
# The tree is look like this:
#    1
# There is one and only one subtree in the tree. So we return 1.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        if not root:
            return root

        self.min_sum = float('inf')
        self.min_root = None
        self.find_min_sum(root)
        return self.min_root

    def find_min_sum(self, root):
        if root is None:
            return 0

        left_subtree = self.find_min_sum(root.left)
        right_subtree = self.find_min_sum(root.right)

        whole_tree = left_subtree + right_subtree + root.val

        if whole_tree < self.min_sum:
            self.min_sum = whole_tree
            self.min_root = root


        return whole_tree


