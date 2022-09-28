# Description
# Write an efficient algorithm that searches for a target value in an m x n matrix.

# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)

# n × m < 50000n×m<50000

# Example 2:
# Input:
# matrix = [
#   [1, 3, 5, 7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output:

# true
# Explanation: The matrix includes 3, return true.

# Challenge
# O(log(n) + log(m)) time

# 一次二分 - O(lognm)	没想到matrix转array的方法
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
            
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = (start + end) // 2
            x, y = mid // m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start // m, start % m
        if matrix[x][y] == target:
            return True
        
        x, y = end // m, end % m
        if matrix[x][y] == target:
            return True
        
        return False
      
# 两次二分 - O(logn+logm)
 class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
            
        first_num = [matrix[i][0] for i in range(len(matrix))]
        pos = self.binarysearch(first_num, target)
        result = self.binarysearch(matrix[pos], target)
        
        if result == len(matrix[pos]) - 1:
            if matrix[pos][-1] == target:
                return True
            else:
                return False
        else:
            if matrix[pos][result] == target:
                return True
            else:
                return False

    def binarysearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                return mid
        
        if nums[right] <= target:
            return right
        elif nums[left] <= target:
            return left
        return -1
