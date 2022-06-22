# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.

# Method: DP
from typing import (
    List,
)

class Solution:
    """
    @param obstacle_grid: A list of lists of integers
    @return: An integer
    """
    def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        if not obstacle_grid or not obstacle_grid[0]:
            return 0

        n, m = len(obstacle_grid), len(obstacle_grid[0])
        dp = [[0] * m for _ in range(n)]

        # 最左一列
        for i in range(n):
            if obstacle_grid[i][0]:
                break
            dp[i][0] = 1 
        # 最上一行
        for j in range(m):
            if obstacle_grid[0][j]:
                break
            dp[0][j] = 1

        # [i][j] 只能从左或者上来
        for i in range(1, n):
            for j in range(1, m):
                if obstacle_grid[i][j]:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n-1][m-1]


