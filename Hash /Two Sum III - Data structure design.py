# Description
# Design and implement a TwoSum class. It should support the following operations: add and find.

# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Wechat reply the 【607】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# add(1); add(3); add(5);
# find(4) // return true
# find(7) // return false


class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.counter = {}

    def add(self, number):
        # write your code here
        if number in self.counter:
            self.counter[number] += 1
        else:
            self.counter[number] = 1
        # self.counter[number] = self.counter.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for key in self.counter:
            diff = value - key
            if diff in self.counter and (diff != key or self.counter[diff] > 1):
                return True
        return False