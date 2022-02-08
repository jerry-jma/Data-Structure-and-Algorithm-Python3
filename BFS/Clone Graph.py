# Description
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

# You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

# Wechat reply question number 137 to get Universal algorithm template . (wechat id : jiuzhang15)

# You need return the node with the same label as the input node.
# How we represent an undirected graph: http://www.lintcode.com/help/graph/

# Example
# Example1

# Input:
# {1,2,4#2,1,4#4,1,2}
# Output:
# {1,2,4#2,1,4#4,1,2}
# Explanation:
# 1------2
#  \     |
#   \    |
#    \   |
#     \  |
#       4

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    # solution 1: BFS
    # 第一步：找到所有的点 第二步：复制所有的点，将映射关系存起来 第三步：找到所有的边，复制每一条边
    def cloneGraph(self, node):
        if not node:
            return
        # all_nodes has all the original nodes
        all_nodes = self.get_nodes(node)

        old_to_new = {}
        for curr_node in all_nodes:
            old_to_new[curr_node] = UndirectedGraphNode(curr_node.label)

        for curr_node in all_nodes:
            new_node = old_to_new[curr_node]
            for neighbor in curr_node.neighbors:
                new_neighbor = old_to_new[neighbor]
                new_node.neighbors.append(new_neighbor)

        return old_to_new[node]

    def get_nodes(self, node):
        queue = collections.deque([node])
        results = set([node])

        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in results:
                    queue.append(neighbor)
                    results.add(neighbor)

        return results


        # solution 2: using dfs
    def cloneGraph(self, node):
        if not node:
            return

        old_to_new = {}
        return self.dfs(node, old_to_new)

    def dfs(self, node, old_to_new):
        if node in old_to_new:
            return old_to_new[node]

        copy_node = UndirectedGraphNode(node.label)
        old_to_new[node] = copy_node

        for neighbor in node.neighbors:
            copy_node.neighbors.append(self.dfs(neighbor, old_to_new))

        return copy_node
