# Description
# Reverse a linked list.

# Wechat reply the 【35】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# The linked list length is less than 100100

# Example
# Example 1:

# Input:

# linked list = 1->2->3->null
# Output:

# 3->2->1->null
# Explanation:

# Reverse Linked List

# Example 2:

# Input:

# linked list = 1->2->3->4->null
# Output:

# 4->3->2->1->null
# Explanation:

# Reverse Linked List

# Challenge
# Reverse it in-place and in one-pass


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head:
            return None
        prev_node = None
        curr_node = head
        following = head
        while curr_node:
            following = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = following
        return prev_node
