# Description
# Merge k sorted linked lists and return it as one sorted list.

# Analyze and describe its complexity.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Example
# Example 1:

# Input:

# lists = [2->4->null,null,-1->null]
# Output:

# -1->2->4->null
# Explanation:

# Merge 2->4->null, nulll and -1->null into an ascending list.

# Example 2:

# Input:

# lists = [2->6->null,5->null,7->null]
# Output:

# 2->5->6->7->null
# Explanation:

# Merge 2->6->null, 5->null and 7->null into an ascending list.

# """
# Definition of ListNode
# class ListNode(object):

#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
# """
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    # # Solution 1: Using Merge Sort
    # def mergeKLists(self, lists):
    #     if not lists:
    #         return None

    #     return self.merge_all_lists(lists, 0, len(lists) - 1)

    # def merge_all_lists(self, lists, start, end):
    #     if start == end:
    #         return lists[start]

    #     middle = (start + end) // 2

    #     left = self.merge_all_lists(lists, start, middle)
    #     right = self.merge_all_lists(lists, middle+1, end)
    #     return self.merge_two_lists(left, right)

    # def merge_two_lists(self, list1, list2):
    #     dummy = ListNode(0)
    #     tail = dummy

    #     while list1 and list2:
    #         if list1.val < list2.val:
    #             tail.next = list1
    #             list1 = list1.next
    #         else:
    #             tail.next = list2
    #             list2 = list2.next
    #         tail = tail.next

    #     if list1:
    #         tail.next = list1
    #     if list2:
    #         tail.next = list2

    #     return dummy.next