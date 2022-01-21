# Description
# Given a linked list, remove the nth node from the end of list and return its head.

# Wechat reply 【174】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# The minimum number of nodes in list is n.

# Example
# Example 1:
# 	Input: list = 1->2->3->4->5->null， n = 2
# 	Output: 1->2->3->5->null


# Example 2:
# 	Input:  list = 5->4->3->2->1->null, n = 2
# 	Output: 5->4->3->1->null
# Challenge
# Can you do it without getting the length of the linked list?

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
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next