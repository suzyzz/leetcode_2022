# Description
# Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human (numbers 0, 1, 2).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

# Example
# Example 1:
# Input:
# [[0,1,2,0,0],
#  [1,0,0,2,1],
#  [0,1,0,0,0]]
# Output:2
  
# Example 2:
# Input:
# [[0,0,0],
#  [0,0,0],
#  [0,0,1]]
# Output:4



from typing import (
    List,
)
import collections
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        n, m, human_count, turn_count = len(grid), len(grid[0]), 0, 0

        # 统计人类数量并将僵尸加入队列
        queue = collections.deque()     
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j))
                elif grid[i][j] == 0:
                    human_count += 1
        
        while queue:
            increase_zombie = 0
            new_zombie_count = len(queue)
            for _ in range(new_zombie_count):
                (x, y) = queue.popleft()
                for direction in DIRECTIONS:
                    new_x, new_y = x + direction[0], y + direction[1]
                    if self.is_valid(new_x, new_y, n, m, grid):
                        print(new_x,new_y)
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 1
                        increase_zombie += 1
            if increase_zombie == 0: # 如果没有新增的僵尸，跳出循环
                break
            human_count -= increase_zombie
            turn_count += 1
            if human_count == 0: # 如果人类都被感染，跳出循环
                break
        
        if human_count > 0:
            return -1
        return turn_count
        
    def is_valid(self, x, y, n, m, grid):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if grid[x][y] != 0:
            return False
        return True


