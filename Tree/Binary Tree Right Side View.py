# Description
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom

# Example
# Example 1

# Input: {1,2,3,#,5,#,4}
# Output: [1,3,4]
# Explanation:
#    1
#  /   \
# 2     3
#  \     \
#   5     4
# Example 2

# Input: {1,2,3}
# Output: [1,3]
# Explanation:
#    1
#  /   \
# 2     3
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    # def rightSideView(self, root):
    #     if not root:
    #         return []

    #     queue = collections.deque()
    #     queue.append(root)
    #     result = []

    #     while queue:
    #         length = len(queue)
    #         temp = []

    #         for i in range(length):
    #             curr_node = queue.popleft()
    #             temp.append(curr_node.val)
    #             if curr_node.left:
    #                 queue.append(curr_node.left)
    #             if curr_node.right:
    #                 queue.append(curr_node.right)

    #         if temp:
    #             result.append(temp[-1])

    #     return result


    def rightSideView(self, root):
        result =[]
        self.helper(root, 0, result)
        return result

    def helper(self, node, depth, result):
        if node:
            if depth == len(result):
                result.append(node.val)
            self.helper(node.right, depth+1, result)
            print('depth after right', depth)
            self.helper(node.left, depth+1, result)
            print('depth after left', depth)











