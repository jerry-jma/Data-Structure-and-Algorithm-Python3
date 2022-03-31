# Description
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Example
# Example 1:

# Input: {}
# Output: 0
# Example 2:

# Input:  {1,#,2,3}
# Output: 3
# Explanation:
# 	1
# 	 \
# 	  2
# 	 /
# 	3
# it will be serialized {1,#,2,3}
# Example 3:

# Input:  {1,2,3,#,#,4,5}
# Output: 2
# Explanation:
#       1
#      / \
#     2   3
#        / \
#       4   5
# it will be serialized {1,2,3,#,#,4,5}


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
    @param root: The root of binary tree
    @return: An integer
    """
    # Solution 1: BFS - Level Traverse
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()

                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


    # Solution 2: DFS
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.min_depth(root.left)
        right_depth = self.min_depth(root.right)

        if left_depth and right_depth:
            return min(left_depth, right_depth) + 1
        # this else could be used to replaced all the remaining conditions
        # else:
        #     return max(left_depth, right_depth) + 1

        elif left_depth == 0:
            return right_depth + 1
        elif right_depth == 0:
            return left_depth + 1
        else:
            return 1
