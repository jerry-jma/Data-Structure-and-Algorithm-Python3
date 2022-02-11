# Description
# Flatten a binary tree to a fake "linked list" in pre-order traversal.

# Here we use the right pointer in TreeNode as the next pointer in ListNode.

# Wechat reply the 【question number】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

# Example
# Example 1:

# Input:{1,2,5,3,4,#,6}
# Output：{1,#,2,#,3,#,4,#,5,#,6}
# Explanation：
#      1
#     / \
#    2   5
#   / \   \
#  3   4   6

# 1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6
# Example 2:

# Input:{1}
# Output:{1}
# Explanation：
#          1
#          1
# Challenge
# Do it in-place without any extra memory.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        self.flatten_and_return_last(root)

    def flatten_and_return_last(self, root):
        if root is None:
            return None

        left_last = self.flatten_and_return_last(root.left)
        right_last = self.flatten_and_return_last(root.right)

        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        return right_last or left_last or root
        # if right_last:
        #     return right_last
        # elif left_last:
        #     return left_last
        # else:
        #     return root

