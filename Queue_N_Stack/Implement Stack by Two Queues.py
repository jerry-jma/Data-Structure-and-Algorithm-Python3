# Description
# Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

# Wechat reply the 【494】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input:
# push(1)
# pop()
# push(2)
# isEmpty() // return false
# top() // return 2
# pop()
# isEmpty() // return true
# Example 2:

# Input:
# isEmpty()

class Stack:

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.q1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        if not self.q1:
            self.q1, self.q2 = self.q2, self.q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        self.q1.popleft()

    """
    @return: An integer
    """
    def top(self):
        if not self.q1:
            self.q1, self.q2 = self.q2, self.q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        return self.q1[0]


    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return len(self.q1) == 0 and len(self.q2) == 0

