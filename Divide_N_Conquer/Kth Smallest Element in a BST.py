# Description
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Wechat reply the 【902】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example
# Example 1:

# Input：{1,#,2},2
# Output：2
# Explanation：
# 	1
# 	 \
# 	  2
# The second smallest element is 2.
# Example 2:

# Input：{2,1,3},1
# Output：1
# Explanation：
#   2
#  / \
# 1   3
# The first smallest element is 1.
# Challenge
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        stack = []

        while root:
            stack.append(root)
            root = root.left

        for i in range(k - 1):
            if not stack:
                return None

            curr_node = stack.pop()
            node = curr_node.right

            while node:
                stack.append(node)
                node = node.left

        return stack[-1].val


