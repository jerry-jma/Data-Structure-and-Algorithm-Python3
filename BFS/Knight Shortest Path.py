# Description
# Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
# Return -1 if destination cannot be reached.

# Wechat reply the 【611】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# source and destination must be empty.
# Knight can not enter the barrier.
# Path length refers to the number of steps the knight takes.
# If the knight is at (x, y), he can get to the following positions in one step:

# (x + 1, y + 2)
# (x + 1, y - 2)
# (x - 1, y + 2)
# (x - 1, y - 2)
# (x + 2, y + 1)
# (x + 2, y - 1)
# (x - 2, y + 1)
# (x - 2, y - 1)
# Example
# Example 1:

# Input:
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2]
# Output: 2
# Explanation:
# [2,0]->[0,1]->[2,2]
# Example 2:

# Input:
# [[0,1,0],
#  [0,0,1],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2]
# Output:-1

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
Directions = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        if not grid:
            return -1

        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            (x, y) = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x,y)]
            for dx, dy in Directions:
                next_x = x + dx
                next_y = y + dy
                if (next_x,next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue
                queue.append((next_x, next_y))
                distance[(next_x, next_y)] = distance[(x,y)] + 1

        return -1

    def is_valid(self, x, y, grid):
        row_length = len(grid) - 1
        col_length = len(grid[0]) - 1

        if x < 0 or x > row_length or y < 0 or y > col_length:
            return False
        if grid[x][y] == 1:
            return False
        if grid[x][y] == 0:
            return True

    #  # solution 2: two-directional BFS
    # def shortestPath(self, grid, source, destination):
    #     if not grid or not grid[0]:
    #         return -1
    #     if grid[destination.x][destination.y] == 1:
    #         return -1
    #     if (source.x, source.y) == (destination.x, destination.y):
    #         return 0

    #     forward_queue = collections.deque([(source.x, source.y)])
    #     forward_visited = set([(source.x, source.y)])
    #     backward_queue = collections.deque([(destination.x, destination.y)])
    #     backward_visisted = set([(destination.x, destination.y)])

    #     distance = 0

    #     while forward_queue and backward_queue:
    #         distance += 1
    #         if self.extend_queue(grid, forward_queue, forward_visited, backward_visisted):
    #             return distance
    #         print(forward_visited, backward_visisted)

    #         distance += 1
    #         if self.extend_queue(grid, backward_queue, backward_visisted, forward_visited):
    #             return distance

    #     return -1


    # def extend_queue(self, grid, queue, visited, opposite_visited):
    #     size = len(queue)
    #     for _ in range(size):
    #         x, y = queue.popleft()
    #         for delta_x, delta_y in Directions:
    #             new_x = delta_x + x
    #             new_y = delta_y + y

    #             if not self.is_valid(grid, new_x, new_y):
    #                 continue
    #             if (new_x,new_y) in visited:
    #                 continue
    #             if (new_x, new_y) in opposite_visited:
    #                 return True
    #             queue.append((new_x, new_y))
    #             visited.add((new_x, new_y))


    #     return False

    # def is_valid(self, grid, x, y):
    #     if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
    #         return False
    #     if grid[x][y] == 1:
    #         return False
    #     if grid[x][y] == 0:
    #         return True



