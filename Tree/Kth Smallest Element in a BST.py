# Description
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)


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

   # Solution 2: dfs in_order travesal
    def kthSmallest(self, root, k):
        if not root:
            return None

        in_order = []
        self.dfs(root, in_order)
        return in_order[k-1]

    def dfs(self, node, in_order):
        if not node:
            return
        self.dfs(node.left,in_order)
        in_order.append(node.val)
        self.dfs(node.right, in_order)