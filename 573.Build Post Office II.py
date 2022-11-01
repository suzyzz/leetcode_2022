# Description
# Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.
# Returns the sum of the minimum distances from all houses to the post office.Return -1 if it is not possible.
# You cannot pass through wall and house, but can pass through empty.
# You only build post office on an empty.

# Example
# Example 1:
# Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
# Output：8
# Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
# Example 2:
# Input：[[0,1,0],[1,0,1],[0,1,0]]
# Output：4
# Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.


# BFS-连通块	- O(n^2 * m^2)

class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        dist = [[sys.maxint for j in range(n)] for i in range(m)]
        reachable_count = [[0 for j in range(n)] for i in range(m)]
        min_dist = sys.maxint
        
        buildings = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, reachable_count)
                    buildings += 1
  
        for i in range(m):
            for j in range(n):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != sys.maxint else -1
        
    def bfs(self, grid, i, j, dist, m, n, reachable_count):
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = collections.deque([(i,j, 0)])
        
        while q:
            i, j, l = q.popleft()
            if dist[i][j] == sys.maxint:
                dist[i][j] = 0
            dist[i][j] += l

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i+x, j+y

                if nx > -1 and nx < m and ny > -1 and ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        q.append((nx, ny, l+1))
                        reachable_count[nx][ny] += 1
