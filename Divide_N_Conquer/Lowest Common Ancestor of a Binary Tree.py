# Description
# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

# Wechat reply question number to get job skills free video package. (wechat id : jiuzhang15)

# Assume two nodes are exist in tree.

# Example
# Example 1:

# Input:

# tree = {1}
# A = 1
# B = 1
# Output:

# 1
# Explanation:

# For the following binary tree（only one node）:
#         1
# LCA(1,1) = 1
# Example 2:

# Input:

# tree = {4,3,7,#,#,5,6}
# A = 3
# B = 5
# Output:

# 4
# Explanation:

# For the following binary tree:

#      4
#     / \
#    3   7
#       / \
#      5   6

# LCA(3, 5) = 4

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # this would work if it's a binary search tree  {-2, 1, 3} 1,3
        # cur = root

        # while cur:
        #     if A.val > cur.val and B.val > cur.val:
        #         cur = cur.right
        #     elif A.val < cur.val and B.val < cur.val:
        #         cur = cur.left
        #     else:
        #         return cur

        if not root:
            return None

        if root == A or root == B:
            return root

        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        # we are assuming we found ancestor,
        # however there are a few cases we need to discuss

        if left and right:
            return root
        if left:
            return left
        if right:
            return right

        return None









