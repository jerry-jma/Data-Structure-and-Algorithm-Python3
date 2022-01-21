# Description
# Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.

# Contact me on wechat to get more FLAMG requent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:
# 	Input: list1 = null, list2 = 0->3->3->null
# 	Output: 0->3->3->null


# Example 2:
# 	Input:  list1 =  1->3->8->11->15->null, list2 = 2->null
# 	Output: 1->2->3->8->11->15->null

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(-1)
        curr_node = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr_node.next = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                l2 = l2.next
            # shift the pointer as we go, so at the end curr_node
            # will be the last node, while dummy.next will be the first
            curr_node = curr_node.next

        if l1: curr_node.next = l1
        if l2: curr_node.next = l2

        return dummy.next



