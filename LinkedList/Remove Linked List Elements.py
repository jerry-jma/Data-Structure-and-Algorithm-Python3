# Description
# Remove all elements from a linked list of integers that have value val.

# Wechat reply the 【452】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input: head = 1->2->3->3->4->5->3->null, val = 3
# Output: 1->2->4->5->null
# Example 2:

# Input: head = 1->1->null, val = 1
# Output: null

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        dummy = ListNode(float('inf'))
        dummy.next = head
        curr_node = dummy
        while curr_node.next:
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return dummy.next
