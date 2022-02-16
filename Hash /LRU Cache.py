# Description
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

# get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# Finally, you need to return the data from each get.

# Wechat reply question number to get job skills free video package. (wechat id : jiuzhang15)

# Example
# Example1

# Input:
# LRUCache(2)
# set(2, 1)
# set(1, 1)
# get(2)
# set(4, 1)
# get(1)
# get(2)
# Output: [1,-1,1]
# Explanation：
# cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
# Example 2:

# Input：
# LRUCache(1)
# set(2, 1)
# get(2)
# set(3, 2)
# get(2)
# get(3)
# Output：[1,-1,2]
# Explanation：
# cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.


class LinkedNode():
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.keyToPrev = {}

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.keyToPrev:
            return -1

        self.kick(key)

        return self.tail.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.keyToPrev:
            self.kick(key)
            self.tail.value = value
            return

        self.push_back(LinkedNode(key, value))

        if len(self.keyToPrev) > self.capacity:
            self.popFront()

    def kick(self, key):
        prev = self.keyToPrev[key]
        key_node = prev.next

        if key_node == self.tail:
            return

        prev.next = key_node.next
        self.keyToPrev[key_node.next.key] = prev
        key_node.next = None

        self.push_back(key_node)

    def push_back(self, key_node):
        self.keyToPrev[key_node.key] = self.tail
        self.tail.next = key_node
        self.tail = key_node

    def popFront(self):
        head = self.dummy.next
        del self.keyToPrev[head.key]
        self.dummy.next = head.next
        self.keyToPrev[head.next.key] = self.dummy


