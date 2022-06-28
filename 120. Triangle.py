# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104

#Method 1: DFS-traversal (TLE)
class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        self.min_sum = float("inf")
        self.dfs_traversal(triangle, 0, 0, 0)
        return self.min_sum
    
    def dfs_traversal(self, triangle, x, y, path_sum):
        if x == len(triangle):
            self.min_sum = min(self.min_sum, path_sum)
            return
        
        self.dfs_traversal(triangle, x + 1, y, path_sum + triangle[x][y])
        self.dfs_traversal(triangle, x + 1, y + 1, path_sum + triangle[x][y])
        
        
#Method 2: DFG-Divide Conquer (TLE)
class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        return self.dfs_divide_conquer(triangle, 0, 0)
    
    def dfs_divide_conquer(self, triangle, x, y):
        if x == len(triangle):
            return 0
        
        left = self.dfs_divide_conquer(triangle, x + 1, y)
        right = self.dfs_divide_conquer(triangle, x + 1, y + 1)
        return min(left, right) + triangle[x][y]
	
#Method 3: DFG-Divide Conquer + Hash - Memoization Search
class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        return self.dfs_divide_conquer(triangle, 0, 0, {})
    
    def dfs_divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0
        if (x,y) in memo:
            return memo[(x, y)]
        left = self.dfs_divide_conquer(triangle, x + 1, y, memo)
        right = self.dfs_divide_conquer(triangle, x + 1, y + 1, memo)
        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]

#Method 4: DP-for-loop-Top-down
class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        n = len(triangle)        
        dp = [[0] * (i + 1) for i in range(n)]
        
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            
        return min(dp[n - 1])

#Method 5: DP-for-loop-Bottom-Up
class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        n = len(triangle)        
        dp = [[0] * (i + 1) for i in range(n)]

        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j +1]) + triangle[i][j]
            
        return dp[0][0]

#Method 6: DP-for-loop-Top-down, rolling array
class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        n = len(triangle)        
        dp = [[0] * n, [0] * n]
        
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]
            dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]

            for j in range(1, i):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], dp[(i - 1) % 2][j]) + triangle[i][j]
            
        return min(dp[(n - 1) % 2])



