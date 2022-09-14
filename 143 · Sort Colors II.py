Description
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
You are not suppose to use the library's sort function for this problem.
k <= n
Example
Example1

Input: 
[3,2,2,1,4] 
4
Output: 
[1,2,2,3,4]
Example2

Input: 
[2,1,1,2,2] 
2
Output: 
[1,1,2,2,2]
Challenge
You can directly use The counting sorting algorithm scan twice, but it will cost O(k) extra memory. Now can you do it in use O(logk) extra memory?

# 当 k 接近 1 时，用计数排序，counting sort，时间O(N)，空间O(k)
# 当 k 在 1 和 N 之间中位数，用彩虹排序，rainbow sort，时间O(nLogK)，空间O(logK)--递归栈的深度
# 当 k 接近 N 时，直接用快速排序。

# Method 1 Rainbow sort- 关答
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        self.sort(colors, 1, k, 0, len(colors) - 1)
        
    def sort(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return
            
        color = (color_from + color_to) // 2 # 重点 1， 定义k的中间值为pivot 而不是quicksort的随机取数 所以时间消耗更稳定
        
        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= color: # 重点 2： 这里是 <= 不是 quicksort的 <, 
              #因为等于的情况不用换=> (left side: 111222, right side 2223333  这样是可以的)， 
              #相比 quicksort是等于也要换 => (left side: 111, right side: 2222222333  必须是这样)
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        
        self.sort(colors, color_from, color, index_from, right)
        self.sort(colors, color + 1, color_to, left, index_to)
        
        
# Method 2 Counting Sort - 关答 - 时间和空间的双赢 
# 这个方法非常直观了 记录每个数出现的次数再重写写出来 colors
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        counter = [0 for _ in range(k+1)]
        
        for color in colors:
            counter[color] += 1 
            
        index = 0
        for color, count in enumerate(counter):
            for _ in range(count):
                colors[index] = color 
                index += 1 





# Method 3 - Merge sort - 非关答 自己写的 
    def sort_colors2(self, colors: List[int], k: int):
        if not colors:
            return colors
        tmp = [0]*len(colors)
        self.mergesort(colors, tmp, 0, len(colors) - 1)

    def mergesort(self, colors, tmp, start, end):
        if start >= end:
            return 
        self.mergesort(colors, tmp, start, (start + end) // 2)
        self.mergesort(colors, tmp, (start + end) // 2 + 1, end)
        self.merge(colors, tmp, start, end)
    
    def merge(self, colors, tmp, start, end):
        mid = (start + end) // 2
        left_index = start 
        right_index = mid + 1
        tmp_index = start
        while left_index <= mid and right_index <= end:
            if colors[left_index] <= colors[right_index]:
                tmp[tmp_index] = colors[left_index]
                tmp_index += 1
                left_index += 1
            else:
                tmp[tmp_index] = colors[right_index]
                tmp_index += 1
                right_index += 1
        while left_index <= mid:
            tmp[tmp_index] = colors[left_index]
            tmp_index += 1
            left_index += 1
        while right_index <= end:
            tmp[tmp_index] = colors[right_index]
            tmp_index += 1
            right_index += 1
        for i in range(start, end + 1):
            colors[i] = tmp[i]
