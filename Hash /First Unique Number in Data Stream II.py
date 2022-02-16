# Description
# We need to implement a data structure named DataStream. There are two methods required to be implemented:

# void add(number) // add a new number
# int firstUnique() // return first unique number
# Wechat reply the 【960】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# You can assume that there must be at least one unique number in the stream when calling the firstUnique.

# Example
# Example 1:

# Input:
# add(1)
# add(2)
# firstUnique()
# add(1)
# firstUnique()
# Output:
# [1,2]
# Example 2:

# Input:
# add(1)
# add(2)
# add(3)
# add(4)
# add(5)
# firstUnique()
# add(1)
# firstUnique()
# add(2)
# firstUnique()
# add(3)
# firstUnique()
# add(4)
# firstUnique()
# add(5)
# add(6)
# firstUnique()
# Output:
# [1,2,3,4,5,6]

class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.dummy = ListNode(0)
        self.tail = self.dummy

        self.num_to_prev = {}
        # if the num appears 2 or more times
        self.duplicates = set()

    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # if it appear more than twice, return
        if num in self.duplicates:
            return

        # the first time it appears
        if num not in self.num_to_prev:
            self.add_to_tail(num)
            return

        # it's in num_to_pre but it's the 2nd time it appear
        self.remove(num)

        self.duplicates.add(num)

    def add_to_tail(self, num):
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    def remove(self, num):
        prev = self.num_to_prev[num]
        prev.next = prev.next.next

        del self.num_to_prev[num]

        # consider if it's the tail or not
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail = prev

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # print(self.dummy.next.val, self.dummy.next.next.val, self.dummy.next.next.next.val)
        if not self.dummy.next:
            return None
        return self.dummy.next.val
