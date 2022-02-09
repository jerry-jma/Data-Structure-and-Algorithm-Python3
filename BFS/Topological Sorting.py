# Description
# Given an directed graph, a topological order of the graph nodes is defined as follow:

# For each directed edge A -> B in graph, A must before B in the order list.
# The first node in the order can be any node in the graph with no nodes direct to it.
# Find any topological order for the given graph.

# Wechat reply the 【127】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# You can assume that there is at least one topological order in the graph.
# Learn more about representation of graphs

# The number of graph nodes <= 5000
# Example
# Example 1:

# Input:

# graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}
# Output:

# [0, 1, 2, 3, 4, 5]
# Explanation:

# For graph as follow:

# 图片

# he topological order can be:
# [0, 1, 2, 3, 4, 5]
# [0, 2, 3, 1, 5, 4]
# ...
# You only need to return any topological order for the given graph.

# Challenge
# Can you do it in both BFS and DFS?

"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        if not graph:
            return None

        result = []

        in_degree = self.get_in_degree(graph)

        # start_node = []
        # for node in in_degree:
        #     if in_degree[node] == 0:
        #         start_node.append(node)
        start_node = [node for node in graph if in_degree[node] == 0]

        queue = collections.deque(start_node)

        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)
            for neighbor in curr_node.neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result

    def get_in_degree(self, graph):
        # make all node with 0 in in degree
        # in_degree = {}
        # for node in graph:
        #     in_degree[node] = 0
        in_degree = {node: 0 for node in graph}

        for node in graph:
            for neighbor in node.neighbors:
                in_degree[neighbor] += 1

        return in_degree




