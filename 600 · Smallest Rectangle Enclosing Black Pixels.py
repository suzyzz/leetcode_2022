# Description
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

# Example
# Example 1:

# Input：["0010","0110","0100"]，x=0，y=2
# Output：6
# Explanation：
# The upper left coordinate of the matrix is (0,1), and the lower right coordinate is (2,2).
# Example 2:

# Input：["1110","1100","0000","0000"], x = 0, y = 1
# Output：6
# Explanation：
# The upper left coordinate of the matrix is (0, 0), and the lower right coordinate is (1,2).

# 关答-两次二分 - O(MlogN+NlogM)

class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def minArea(self, image, x, y):
        # Write your code here
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        if n == 0:
            return 0

        start = y
        end = n - 1
        while start < end:
            mid = start + (end - start) / 2 + 1
            if self.checkColumn(image, mid):
                start = mid
            else:
                end = mid - 1

        right = start

        start = 0
        end = y
        while start < end:
            mid = start + (end - start) / 2
            if self.checkColumn(image, mid):
                end = mid
            else:
                start = mid + 1

        left = start
        
        start = x
        end = m - 1
        while start < end:
            mid = start + (end - start) / 2 + 1
            if self.checkRow(image, mid):
                start = mid
            else:
                end = mid - 1

        down = start
        
        start = 0
        end = x
        while start < end:
            mid = start + (end - start) / 2
            if self.checkRow(image, mid):
                end = mid
            else:
                start = mid + 1

        up = start
        
        return (right - left + 1) * (down - up + 1)

    def checkColumn(self, image, col):
        for i in xrange(len(image)):
            if image[i][col] == '1':
                return True
        return False

    def checkRow(self, image, row):
        for j in xrange(len(image[0])):
            if image[row][j] == '1':
                return True
        return False
