# Description
# Write an efficient algorithm that searches for a value in an m x n matrix, return The number of occurrence of it.

# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# Integers in each column are sorted from up to bottom.
# No duplicate integers in each row or column.

# Example
# Example 1:
# Input:
# matrix = [[3,4]]
# target = 3
# Output:
# 1
# Explanation:There is only one 3 in the matrix.

# Example 2:
# Input:
# matrix = [
#       [1, 3, 5, 7],
#       [2, 4, 7, 8],
#       [3, 5, 9, 10]
#     ]
# target = 3
# Output:
# 2
# Explanation:There are two 3 in the matrix.

# Challenge
# O(m+n) time and O(1) extra space

# 二分 - O(n+m)	一遍写出关答

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix) - 1, len(matrix[0]) - 1
        i, j, count = n, 0, 0
        while i >= 0 and j <= m:
            if matrix[i][j] == target:
                count += 1
                i, j = i - 1, j + 1
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return count
