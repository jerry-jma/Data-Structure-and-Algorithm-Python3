# Description
# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 \leq n \leq 10^41≤n≤10
# 4
#  . Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

# Example
# Example 1:

# Input:org = [1,2,3], seqs = [[1,2],[1,3]]
# Output: false
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
# Example 2:

# Input: org = [1,2,3], seqs = [[1,2]]
# Output: false
# Explanation:
# The reconstructed sequence can only be [1,2].
# Example 3:

# Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
# Output: true
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
# Example 4:

# Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
# Output:true

from typing import (
    List,
)

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        all_nodes = set()
        for seq in seqs:
            for node in seq:
                all_nodes.add(node)

        in_degrees = {node: 0 for node in all_nodes}
        neighbors = {node: [] for node in all_nodes}

        for seq in seqs:
            for i in range(len(seq) - 1):
                neighbors[seq[i]].append(seq[i+1])
                in_degrees[seq[i+1]] += 1

        queue = collections.deque()
        order = []

        for node in all_nodes:
            if in_degrees[node] == 0:
                queue.append(node)

        while queue:
            if len(queue) > 1:
                return False

            curr = queue.popleft()
            order.append(curr)

            for neighbor in neighbors[curr]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return order == org









