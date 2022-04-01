# Description
# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

# 1.1≤N≤200.
# 2.M[i][i] = 1 for all students.
# 3.If M[i][j] = 1, then M[j][i] = 1.

# Example
# Example 1:

# Input: [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Explanation:
# The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:

# Input: [[1,1,0],[1,1,1],[0,1,1]]
# Output: 1
# Explanation:
# The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

from typing import (
    List,
)

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    """
    @param m: a matrix
    @return: the total number of friend circles among all the students
    """
    def find_circle_num(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        visited = set()
        circles = 0

        for i in range(len(M)):
            if i not in visited:
                circles += 1
                self.bfs(M, i, visited)

        return circles

    def bfs(self, M, i, visited):
        queue = collections.deque([i])
        visited.add(i)

        while queue:
            x = queue.popleft()
            for y in range(len(M[0])):
                if x == y:
                    continue
                if M[x][y] == 1 and y not in visited:
                    queue.append(y)
                    visited.add(y)

















