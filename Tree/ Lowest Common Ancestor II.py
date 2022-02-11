# Description
# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

# The nearest common ancestor of two nodes refers to the nearest common node among all the parent nodes of two nodes (including the two nodes).

# In addition to the left and right son pointers, each node also contains a father pointer, parent, pointing to its own father.

# Wechat reply the 【474】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input：{4,3,7,#,#,5,6},3,5
# Output：4
# Explanation：
#      4
#      / \
#     3   7
#        / \
#       5   6
# LCA(3, 5) = 4
# Example 2:

# Input：{4,3,7,#,#,5,6},5,6
# Output：7
# Explanation：
#       4
#      / \
#     3   7
#        / \
#       5   6
# LCA(5, 6) = 7


"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        ancestors = set()

        curr = A
        while curr:
            ancestors.add(curr)
            curr = curr.parent

        curr = B
        while curr:
            if curr in ancestors:
                return curr
            curr = curr.parent

        return None
