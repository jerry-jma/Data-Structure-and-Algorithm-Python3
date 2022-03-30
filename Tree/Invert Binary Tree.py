# Description
# Invert a binary tree.Left and right subtrees exchange.

# Example
# Example 1:

# Input: {1,3,#}
# Output: {1,#,3}
# Explanation:
# 	  1    1
# 	 /  =>  \
# 	3        3
# Example 2:

# Input: {1,2,3,#,#,4}
# Output: {1,3,2,#,4}
# Explanation:

#       1         1
#      / \       / \
#     2   3  => 3   2
#        /       \
#       4         4
# Challenge
# Do it in recursion is acceptable, can you do it without recursion?

from lintcode import (
    TreeNode,
)

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
    # Solution 1: recursion
    # def invert_binary_tree(self, root: TreeNode):
        # if not root:
        #     return None

        # # if not root.left and not root.right:
        # #     return root

        # left = self.invert_binary_tree(root.left)
        # right = self.invert_binary_tree(root.right)

        # root.right = left
        # root.left = right

        # return root

    # Solution 2: Iteration
    def invert_binary_tree(self, root: TreeNode):
        if not root:
            return

        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)









