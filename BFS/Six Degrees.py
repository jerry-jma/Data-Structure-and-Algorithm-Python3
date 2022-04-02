# Description
# Six degrees of separation is a philosophical problem, which means that everyone and everything can be connected through six steps or less.

# Now give you a friendship, calculate how many steps two people can be connected through, if not, return -1.

# Example
# Example1

# Input: {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4
# Output: 2
# Explanation:
#     1------2-----4
#      \          /
#       \        /
#        \--3--/
# Example2

# Input: {1#2,4#3,4#4,2,3} and s = 1, t = 4
# Output: -1
# Explanation:
#     1      2-----4
#                  /
#                /
#               3


"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        queue = collections.deque([s])
        visited = {}
        visited[s] = 0

        while queue:
            node = queue.popleft()

            if node.label == t.label:
                return visited[node]

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = visited[node] + 1

        return -1








