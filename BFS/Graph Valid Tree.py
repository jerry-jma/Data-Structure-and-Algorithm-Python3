# Description
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example
# Example 1:

# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.
# Example 2:

# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.


from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    # tree 无环 但是是都联通的
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: #note: 如果无环， 5个node，只能一共有4条边
            return False

        # neighbors = collections.defaultdict(list)
        # similiar to course schedule
        neighbors = {i: [] for i in range(n) }
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)

        # print(neighbors)
        queue = collections.deque([0])
        visited = set([0])

        while queue:
            curr = queue.popleft()
            visited.add(curr)
            for neighbor in neighbors[curr]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        # check 是否都联通了
        return len(visited) == n




