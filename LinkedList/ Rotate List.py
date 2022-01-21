# Description
# Given a list, rotate the list to the right by k places, where k is non-negative.

# Wechat reply the 【170】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input:1->2->3->4->5  k = 2
# Output:4->5->1->2->3
# Example 2:

# Input:3->2->1  k = 1
# Output:1->3->2

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def rotateRight(self, head, k):
        # write your code here
        if not head:
            return None
        if k == 0:
            return head
        k = k % self.getLength(head)
        dummy = ListNode(0)
        dummy.next = head
        ahead = dummy
        for _ in range(k):
            ahead = ahead.next
        print(ahead.val)
        behind = dummy
        while ahead.next:
            behind = behind.next
            ahead = ahead.next
        ahead.next = dummy.next
        dummy.next = behind.next
        behind.next = None

        return dummy.next







