# Description
# Given an integer matrix. Find the longest increasing continuous subsequence in this matrix and return the length of it.
# The longest increasing continuous subsequence here can start at any position and go up/down/left/right.

# Example
# Example 1:

# Input: 
#     [
#       [1, 2, 3, 4, 5],
#       [16,17,24,23,6],
#       [15,18,25,22,7],
#       [14,19,20,21,8],
#       [13,12,11,10,9]
#     ]
# Output: 25
# Explanation: 1 -> 2 -> 3 -> 4 -> 5 -> ... -> 25 (Spiral from outside to inside.)

# Method 1: DP
from typing import (
    List,
)

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def longest_continuous_increasing_subsequence2(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        n, m = len(matrix), len(matrix[0])
        points = []
        for i in range(n):
            for j in range(m):
                points.append((matrix[i][j], i, j))
                
        points.sort()
        
        longest_hash = {}
        for i in range(len(points)):
            key = (points[i][1], points[i][2])
            longest_hash[key] = 1
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                x, y = points[i][1] + dx, points[i][2] + dy
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if (x, y) in longest_hash and matrix[x][y] < points[i][0]:
                    longest_hash[key] = max(longest_hash[key], longest_hash[(x, y)] + 1)
                    
        return max(longest_hash.values())
