# Description
# As the title described, you should only use two stacks to implement a queue's actions.

# The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

# Both pop and top methods should return the value of first element.

# Wechat reply the 【40】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Suppose the queue is not empty when the pop() function is called.

# Example
# Example 1:

# Input:

# Queue Operations =
#     push(1)
#     pop()
#     push(2)
#     push(3)
#     top()
#     pop()
# Output:

# 1
# 2
# 2
# Explanation:

# Both pop and top methods should return the value of the first element.

# Example 2:

# Input:

# Queue Operations =
#     push(1)
#     push(2)
#     push(2)
#     push(3)
#     push(4)
#     push(5)
#     push(6)
#     push(7)
#     push(1)
# Output:

# []
# Explanation:

# There is no output.

# Challenge
# implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.


class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


