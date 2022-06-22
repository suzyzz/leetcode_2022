# Description
# Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.

# If the knight is at (x, y), he can get to the following positions in one step:

# (x + 1, y + 2)
# (x - 1, y + 2)
# (x + 2, y + 1)
# (x - 2, y + 1)
# Example
# Example 1:

# Input:
# [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# Output:
# 3
# Explanation:
# [0,0]->[2,1]->[0,2]->[2,3]
# Example 2:

# Input:
# [[0,1,0],[0,0,1],[0,0,0]]
# Output:
# -1

# 使用双向宽度优先搜索算法

FORWARD_DIRECTIONS = (
    (1, 2),
    (-1, 2),
    (2, 1),
    (-2, 1),
)

BACKWARD_DIRECTIONS = (
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1),
)

class Solution:
    def shortestPath2(self, grid):
        if not grid or not grid[0]:
            return -1
            
        n, m = len(grid), len(grid[0])
        if grid[n - 1][m - 1]:
            return -1
        if n * m == 1:
            return 0
            
        forward_queue = collections.deque([(0, 0)])
        forward_set = set([(0, 0)])
        backward_queue = collections.deque([(n - 1, m - 1)])
        backward_set = set([(n - 1, m - 1)])
        
        distance = 0
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(forward_queue, FORWARD_DIRECTIONS, forward_set, backward_set, grid):
                return distance
                
            distance += 1
            if self.extend_queue(backward_queue, BACKWARD_DIRECTIONS, backward_set, forward_set, grid):
                return distance

        return -1
                
    def extend_queue(self, queue, directions, visited, opposite_visited, grid):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = (x + dx, y + dy)
                if not self.is_valid(new_x, new_y, grid, visited):
                    continue
                if (new_x, new_y) in opposite_visited:
                    return True
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                
        return False
        
    def is_valid(self, x, y, grid, visited):
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y]:
            return False
        if (x, y) in visited:
            return False
        return True

    
    
#   Method 2 - DP

from typing import (
    List,
)

DIRECTIONS = [(-1, -2), (1, -2), (-2, -1), (2, -1)]
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        if not grid or not grid[0]:
            return -1

        n, m = len(grid), len(grid[0])
        dp = [[float('inf')] * m for _ in range(n)]

        dp[0][0] = 0

        for j in range(m):
            for i in range(n):
                if grid[i][j]:
                    continue
                for delta_x, delta_y in DIRECTIONS:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        dp[i][j] = min(dp[i][j], dp[x][y] + 1)
        
        if dp[n - 1][m - 1] == float('inf'):
            return -1
        return dp[n - 1][m - 1]
