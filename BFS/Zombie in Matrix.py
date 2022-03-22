# Description
# Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human (numbers 0, 1, 2).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

# Example
# Example 1:

# Input:
# [[0,1,2,0,0],
#  [1,0,0,2,1],
#  [0,1,0,0,0]]
# Output:
# 2
# Example 2:

# Input:
# [[0,0,0],
#  [0,0,0],
#  [0,0,1]]
# Output:
# 4

from typing import (
    List,
)
DIRECTIONS = [
    (1,0),
    (-1,0),
    (0, -1),
    (0, 1),
]

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        queue = collections.deque()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    queue.append((x,y))

        days = self.bfs(grid, queue, 0)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    return -1

        return days

    def bfs(self, grid, queue, days):
        while queue:
            size = len(queue)
            days += 1
            for _ in range(size):
                x, y = queue.popleft()
                for delta_x, delta_y in DIRECTIONS:
                    new_x = delta_x + x
                    new_y = delta_y + y
                    if not self.is_valid(grid, new_x, new_y):
                        continue
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y))
        return days - 1

    def is_valid(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])

        if not (0 <= x < m and 0 <= y < n):
            return False
        if grid[x][y] == 2:
            return False
        if grid[x][y] == 1:
            return False
        if grid[x][y] == 0:
            return True






