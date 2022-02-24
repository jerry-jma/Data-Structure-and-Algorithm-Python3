# Description
# Given a linked list, determine if it has a cycle in it.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# The length of the linked list does not exceed 10000.

# Example
# Example 1:

# Input:

# linked list = 21->10->4->5，then tail connects to node index 1(value 10).
# Output:

# true
# Explanation:

# The linked list has rings.

# Example 2:

# Input:

# linked list = 21->10->4->5->null
# Output:

# false
# Explanation:

# The linked list has no rings.

# Challenge
# Can you solve it without using extra space?


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False