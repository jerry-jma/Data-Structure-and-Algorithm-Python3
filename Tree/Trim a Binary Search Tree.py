# Description
# Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the new tree are between min and max (inclusive). The resulting tree should still be a valid binary search tree. So, if we get this tree as input:
# http://www.ardendertat.com/wp-content/uploads/2012/01/bst.png
# and we’re given min value as 5 and max value as 13, then the resulting binary search tree should be:
# http://www.ardendertat.com/wp-content/uploads/2012/01/bst_trim.png

# Example
# Example1

# Input:
# {8,3,10,1,6,#,14,#,#,4,7,13}
# 5
# 13
# Output: {8, 6, 10, #, 7, #, 13}
# Explanation:
# The picture of tree is in the description.
# Example2

# Input:
# {1,0,2}
# 1
# 2
# Output: {1,#,2}
# Explanation:
# Input is
#   1
#  / \
# 0   2
# Output is
#   1
#    \
#     2

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree
    """
    def trimBST(self, root, minimum, maximum):
        # write your code here
        if not root:
            return None
        value = root.val
        if value < minimum:
            return self.trimBST(root.right, minimum, maximum)
        if value > maximun:
            return self.trimBST(root.left, minimum, maximum)
        else:
          root.left = self.trimBST(root.left, minimum, maximum)
          root.right = self.trimBST(root.right, minimum, maximum)
          return root
