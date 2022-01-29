# Description
# Design an iterator over a binary search tree with the following rules:
# Next() returns the next smallest element in the BST.

# Elements are visited in ascending order (i.e. an in-order traversal)
# next() and hasNext() queries run in O(1)O(1) time in average.
# Wechat reply question number to get job skills free video package. (wechat id : jiuzhang15)

# Example
# Example 1:

# Input:

# tree = {10,1,11,#,6,#,12}
# Output:

# [1,6,10,11,12]
# Explanation:

# The BST is look like this:
# 10
# / \
# 1     11
# \      \
# 6       12
# You can return the inorder traversal of a BST [1, 6, 10, 11, 12]

# Example 2:

# Input:

# tree = {2,1,3}
# Output:

# [1,2,3]
# Explanation:

# The BST is look like this:
# 2
# /  \
# 1     3
# You can return the inorder traversal of a BST [1,2,3]

# Challenge
# Extra memory usage O(h), h is the height of the tree.

# Super Star: Extra memory usage O(1)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    # this template is easy to find prev
    def _next(self):
        # write your code here
        curr_node = self.stack[-1]
        if curr_node.right != None:
            temp = curr_node.right
            while temp is not None:
                self.stack.append(temp)
                temp = temp.left
        else:
            node = self.stack.pop()
            while self.stack and self.stack[-1].right == node:
                node = self.stack.pop()

        return curr_node

    # def _next(self):
    #     if self.stack:
    #         curr_node = self.stack.pop()
    #         node = curr_node.right
    #         while node:
    #             self.stack.append(node)
    #             node = node.left
    #         return curr_node






