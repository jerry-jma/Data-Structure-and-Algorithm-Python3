# Description
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

# Find the number of islands.

# Contact me on wechat to get more FLAMG requent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input:
# [
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [0,0,0,1,1],
#   [0,0,0,0,0],
#   [0,0,0,0,1]
# ]
# Output:
# 3
# Example 2:

# Input:
# [
#   [1,1]
# ]
# Output:
# 1

Direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid:
            return 0

        visited = set()
        num_of_Island = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    self.bfs(grid, r, c, visited)
                    num_of_Island += 1

        return num_of_Island

    def bfs(self, grid, r, c, visited):
        queue = collections.deque([(r, c)])
        visited.add((r, c))

        while queue:
            row_idx, col_idx = queue.popleft()
            for dir_x, dir_y in Direction:
                next_r = row_idx + dir_x
                next_c = col_idx + dir_y
                if not self.isValid(grid, next_r, next_c, visited):
                    continue

                queue.append((next_r, next_c))
                visited.add((next_r, next_c))

    def isValid(self, grid, next_r, next_c, visited):
        if next_r not in range(len(grid)):
            return False
        if next_c not in range(len(grid[0])):
            return False
        if (next_r, next_c) in visited:
            return False
        return grid[next_r][next_c]












