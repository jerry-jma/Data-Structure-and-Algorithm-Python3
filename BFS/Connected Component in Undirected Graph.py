# Description
# Find connected component in undirected graph.

# Each node in the graph contains a label and a list of its neighbors.

# (A connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

# You need return a list of label set.

# Nodes in a connected component should sort by label in ascending order. Different connected components can be in any order.
# Learn more about representation of graphs

# Example
# Example 1:

# Input: {1,2,4#2,1,4#3,5#4,1,2#5,3}
# Output: [[1,2,4],[3,5]]
# Explanation:

#   1------2  3
#    \     |  |
#     \    |  |
#      \   |  |
#       \  |  |
#         4   5
# Example 2:

# Input: {1,2#2,1}
# Output: [[1,2]]
# Explanation:

#   1--2

from typing import (
    List,
)
from lintcode import (
    UndirectedGraphNode,
)

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        if not nodes:
            return []

        queue = collections.deque()
        visited = set()
        result = []

        for node in nodes:
            print('before', node.label)
            if node in visited:
                print('is visited', node.label)
                continue
            print('not visited', node.label)
            subgraph = []
            self.bfs(queue, visited, node, subgraph)
            result.append(sorted(subgraph))

        return result

    def bfs(self, queue, visited, node, subgraph):
        queue.append(node)
        visited.add(node)

        while queue:
            curr = queue.popleft()
            subgraph.append(curr.label)
            for neighbor in curr.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)





