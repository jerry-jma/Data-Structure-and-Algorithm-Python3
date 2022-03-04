# Description
# Implement a stack with following functions:

# push(val) push val into the stack
# pop() pop the top element and return it
# min() return the smallest number in the stack
# All above should be in O(1) cost

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# min() will never be called when there is no number in the stack.

# Example
# Example 1:

# Input:

# push(1)
# min()
# push(2)
# min()
# push(3)
# min()
# Output:

# 1
# 1
# 1

class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        self.stack.append(number)

        if len(self.min_stack) == 0:
            self.min_stack.append(number)
        else:
            self.min_stack.append(min(number, self.min_stack[-1]))

    """
    @return: An integer
    """
    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """
    def min(self):
        return self.min_stack[-1]
