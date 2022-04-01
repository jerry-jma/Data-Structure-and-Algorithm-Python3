# Description
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

# 1.There is only one ball and one destination in the maze.
# 2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# 3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# 5.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

# Example
# Example 1:

# Input:
# map =
# [
#  [0,0,1,0,0],
#  [0,0,0,0,0],
#  [0,0,0,1,0],
#  [1,1,0,1,1],
#  [0,0,0,0,0]
# ]
# start = [0,4]
# end = [3,2]
# Output:
# false
# Example 2:

# Input:
# map =
# [[0,0,1,0,0],
#  [0,0,0,0,0],
#  [0,0,0,1,0],
#  [1,1,0,1,1],
#  [0,0,0,0,0]
# ]
# start = [0,4]
# end = [4,4]
# Output:
# true

from typing import (
    List,
)
DIRECTIONS = [
    (1,0),
    (-1,0),
    (0, -1),
    (0,1),
]
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = collections.deque([start])
        visited = set([(start[0], start[1])])

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination[0], destination[1]):
                return True

            for delta_x, delta_y in DIRECTIONS:
                new_x = delta_x + x
                new_y = delta_y + y

                while self.is_valid(maze, new_x, new_y):
                    new_x += delta_x
                    new_y += delta_y

                # ball is stop on the wall, need to backtrack one position,
                # one position before the wall
                new_x -= delta_x
                new_y -= delta_y

                if (new_x, new_y) in visited:
                    continue

                visited.add((new_x, new_y))
                queue.append((new_x, new_y))


        return False

    def is_valid(self, maze, x, y):
        m = len(maze)
        n = len(maze[0])

        if not (0 <= x < m and 0 <= y < n):
            return False
        if maze[x][y] == 1:
            return False

        return True




