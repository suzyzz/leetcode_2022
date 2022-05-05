# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

#自己写 意思对了 慢 321
import collections

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
class Solution:
    def num_islands(self, grid):
        num = 0
        if not grid:
            return num

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                if not grid[i][j]:
                    visited.add((i, j))
                    continue
                num += 1
                self.mark_new_island(i, j, visited, grid)
        return num

    def mark_new_island(self, i, j, visited, grid):
        queue = collections.deque([(i, j)])
        visited.add((i, j))
        while queue:
            (x, y) = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y

                if (next_x, next_y) in visited:
                    continue
                if next_x < 0 or next_x > len(grid) - 1 or next_y < 0 or next_y > len(grid[0]) - 1:
                    continue
                if grid[next_x][next_y]:
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    
                    
                    
                    
                    
#关答 262ms  
from collections import deque

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
                    
        return islands                    
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]
