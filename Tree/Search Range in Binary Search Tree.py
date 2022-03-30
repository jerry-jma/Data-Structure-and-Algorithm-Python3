# Description
# Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.

# Example
# Example 1:

# Input:

# tree = {5}
# k1 = 6
# k2 = 10
# Output:

# []
# Explanation:

# No number between 6 and 10

# Example 2:

# Input:

# tree = {20,8,22,4,12}
# k1 = 10
# k2 = 22
# Output:

# [12,20,22]
# Explanation:

# [12,20,22] between 10 and 22

from typing import (
    List,
)
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        if not root:
            return []
        result = []
        self.search(root, k1, k2, result)
        # result.sort()
        return result

    def search(self, node, lower, upper, result):
        # exit
        if not node:
            return

        if node.val < lower:
            self.search(node.right, lower, upper, result)
        if lower <= node.val <= upper:
            self.search(node.left, lower, upper, result)
            result.append(node.val)
            self.search(node.right, lower, upper, result)
        if node.val > upper:
            self.search(node.left, lower, upper, result)


        # if node.val > lower:
        #     self.search(node.left, lower, upper, result)
        # if lower <= node.val <= upper:
        #     result.append(node.val)
        # if node.val < upper:
        #     self.search(node.right, lower, upper, result)









