# Description
# Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with maximum average.

# Example
# Example 1

# Input：
# {1,-5,11,1,2,4,-2}
# Output：11
# Explanation:
# The tree is look like this:
#      1
#    /   \
#  -5     11
#  / \   /  \
# 1   2 4    -2
# The average of subtree of 11 is 4.3333, is the maximun.
# Example 2

# Input：
# {1,-5,11}
# Output：11
# Explanation:
#      1
#    /   \
#  -5     11
# The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximun.


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree

    def findSubtree2(self, root):
        if not root:
            return None
        self.max_avg = -float('inf')
        self.max_node = None

        self.dfs(root)
        return self.max_node

    def dfs(self, node):
        if not node:
            return 0, 0

        left_sum,left_count = self.dfs(node.left)
        right_sum, right_count = self.dfs(node.right)

        total_sum = left_sum + right_sum + node.val
        total_count = left_count + right_count + 1

        avg = total_sum / total_count
        if avg > self.max_avg:
            self.max_avg = avg
            self.max_node = node

        return total_sum, total_count


