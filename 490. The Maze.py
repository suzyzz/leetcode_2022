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



# BFS -O(n+m）
from typing import (
    List,
)
import collections
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n, m = len(maze), len(maze[0])
        queue = collections.deque([(start[0], start[1])])
        visited = {start[0] * n + start[1]}
        while queue:
            (x, y) = queue.popleft() 
            for (delta_x, delta_y) in DIRECTIONS:
                new_x, new_y = x + delta_x, y + delta_y
                while not self.is_stop(maze, new_x, new_y):
                    new_x, new_y = new_x + delta_x, new_y + delta_y
                new_x -= delta_x
                new_y -= delta_y
                if x == destination[0] and y == destination[1]:
                    return True
                if new_x * n + new_y in visited:
                    continue
                else:
                    visited.add(new_x * n + new_y)
                    queue.append((new_x, new_y))               
        return False

        
    def is_stop(self, maze, new_x, new_y):
        if new_x < 0 or new_x > len(maze) - 1 or new_y < 0 or new_y > len(maze[0]) - 1:
            return True
        if maze[new_x][new_y]:
            return True
        return False
