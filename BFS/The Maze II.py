# Description
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

# 1.There is only one ball and one destination in the maze.
# 2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# 3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# 4.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

# Example
# Example 1:
# 	Input:
# 	(rowStart, colStart) = (0,4)
# 	(rowDest, colDest)= (4,4)
# 	0 0 1 0 0
# 	0 0 0 0 0
# 	0 0 0 1 0
# 	1 1 0 1 1
# 	0 0 0 0 0

# 	Output:  12

# 	Explanation:
# 	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)

# Example 2:
# 	Input:
# 	(rowStart, colStart) = (0,4)
# 	(rowDest, colDest)= (0,0)
# 	0 0 1 0 0
# 	0 0 0 0 0
# 	0 0 0 1 0
# 	1 1 0 1 1
# 	0 0 0 0 0

# 	Output:  6

# 	Explanation:
# 	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(0,0)

DIRECTIONS = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
]

from typing import (
    List,
)

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        queue = collections.deque([start])
        visited = {(start[0], start[1]): 0}
        shortest = float('inf')

        while queue:
            x, y = queue.popleft()

            for delta_x, delta_y in DIRECTIONS:
                new_x = delta_x + x
                new_y = delta_y + y
                steps = 0

                while self.is_valid(maze, new_x, new_y):
                    new_x += delta_x
                    new_y += delta_y
                    steps += 1

                new_x -= delta_x
                new_y -= delta_y

                if ((new_x,new_y)) not in visited or visited[(x,y)] + steps < visited[(new_x,new_y)]:
                    queue.append((new_x, new_y))
                    visited[(new_x, new_y)] = visited[(x, y)] + steps

                # there might be quite a few path will hit the destination
                # the first path might NOT be the shortest one
                # which is why BFS should NOT RETURN right after hit the destination
                if (new_x, new_y) == (destination[0], destination[1]):
                    shortest = min(shortest, visited[(new_x, new_y)])
                    print(shortest, visited[(new_x, new_y)])

        if shortest != float('inf'):
            return shortest
        return -1

    def is_valid(self, maze, x, y):
        m, n = len(maze), len(maze[0])

        if not (0 <= x < m and 0 <= y < n):
            return False

        if maze[x][y] == 1:
            return False

        return True



