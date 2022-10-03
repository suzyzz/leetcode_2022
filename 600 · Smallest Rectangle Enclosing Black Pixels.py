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
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        if not image or not image[0]:
            return 0

        n, m = len(image), len(image[0])
        up = self.binarySearch(image, 0, x, self.getRowColor, '1')
        down = self.binarySearch(image, x, n - 1, self.getRowColor, '0')
        left = self.binarySearch(image, 0, y, self.getColumnColor, '1')
        right = self.binarySearch(image, y, m - 1, self.getColumnColor, '0')

        return (down - up) * (right - left)

    def binarySearch(self, image, start, end, getColorFunc, color):
        # 在 start 到 end 这段区间内
        # 找到第一个 index 使得 getColorFunc(index) == color
        while start + 1 < end:
            mid = (start + end) // 2
            if getColorFunc(image, mid) == color:
                end = mid
            else:
                start = mid
        if getColorFunc(image, start) == color:
            return start
        if getColorFunc(image, end) == color:
            return end
        return end + 1

    def getRowColor(self, image, rowIndex):
        for i in range(len(image[0])):
            if image[rowIndex][i] == '1':
                return '1'
        return '0'

    def getColumnColor(self, image, colIndex):
        for i in range(len(image)):
            if image[i][colIndex] == '1':
                return '1'
        return '0'class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        if not image or not image[0]:
            return 0

        n, m = len(image), len(image[0])
        up = self.binarySearch(image, 0, x, self.getRowColor, '1')
        down = self.binarySearch(image, x, n - 1, self.getRowColor, '0')
        left = self.binarySearch(image, 0, y, self.getColumnColor, '1')
        right = self.binarySearch(image, y, m - 1, self.getColumnColor, '0')

        return (down - up) * (right - left)

    def binarySearch(self, image, start, end, getColorFunc, color):
        # 在 start 到 end 这段区间内
        # 找到第一个 index 使得 getColorFunc(index) == color
        while start + 1 < end:
            mid = (start + end) // 2
            if getColorFunc(image, mid) == color:
                end = mid
            else:
                start = mid
        if getColorFunc(image, start) == color:
            return start
        if getColorFunc(image, end) == color:
            return end
        return end + 1

    def getRowColor(self, image, rowIndex):
        for i in range(len(image[0])):
            if image[rowIndex][i] == '1':
                return '1'
        return '0'

    def getColumnColor(self, image, colIndex):
        for i in range(len(image)):
            if image[i][colIndex] == '1':
                return '1'
        return '0'
