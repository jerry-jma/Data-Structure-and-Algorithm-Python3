# Description
# Insert a node in a sorted linked list.

# Wechat reply the 【219】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input: head = 1->4->6->8->null, val = 5
# Output: 1->4->5->6->8->null
# Example 2:

# Input: head = 1->null, val = 2
# Output: 1->2->null

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        dummy = ListNode(float('inf'))
        dummy.next = head
        curr_node = dummy
        while curr_node.next and curr_node.next.val < val:
            curr_node = curr_node.next
        new_node = ListNode(val)
        new_node.next = curr_node.next
        curr_node.next = new_node

        return dummy.next