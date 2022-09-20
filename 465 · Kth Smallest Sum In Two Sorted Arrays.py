# Description
# Given two integer arrays sorted in ascending order and an integer k. Define sum = a + b, where a is an element from the first array and b is an element from the second one. Find the kth smallest sum out of all possible sums.

# Example
# Example 1

# Input:
# a = [1, 7, 11]
# b = [2, 4, 6]
# k = 3
# Output: 7
# Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 3th is 7.
# Example 2

# Input:
# a = [1, 7, 11]
# b = [2, 4, 6]
# k = 4
# Output: 9
# Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 4th is 9.
# Example 3

# Input:
# a = [1, 7, 11]
# b = [2, 4, 6]
# k = 8
# Output: 15
# Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 8th is 15.
# Challenge
# Do it in either of the following time complexity:

# O(k log min(n, m, k)). where n is the size of A, and m is the size of B.
# O( (m + n) log maxValue). where maxValue is the max number in A and B.

# 贪心 优先队列 O(KlogN)
from typing import (
    List,
)
from heapq import *
class Solution:
    """
    @param a: an integer arrays sorted in ascending order
    @param b: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kth_smallest_sum(self, A: List[int], B: List[int], k: int) -> int:
        heap = []
        for i in range(len(B)):
            heappush(heap, [A[0] + B[i], 0, i])
        while k > 1:
            k -= 1
            # 取出堆中最小值
            point = heappop(heap)
            value = point[0]
            aIdx = point[1]
            bIdx = point[2]
            # 已经是所在数组的最后一个元素了
            if (aIdx == len(A) - 1):
                continue
            else:
                # 压入该数组的下一个元素
                newvalue = A[aIdx + 1] + B[bIdx]
                heappush(heap, [newvalue, aIdx + 1, bIdx])
        return heappop(heap)[0]

      
# 二分 双指针 O(NlongMlogMX)
from heapq import *
class Solution:
    """
    @param a: an integer arrays sorted in ascending order
    @param b: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kth_smallest_sum(self, A: List[int], B: List[int], k: int) -> int:
        n = len(A)
        m = len(B)
        # 二分上下界
        left = A[0] + B[0] - 1
        right = A[n - 1] + B[m - 1] + 1
        while left + 1 < right:
            # 如果小于等于x的超过k个就缩小上界，否则提高下界
            mid = (int)(left + (right - left) // 2)
            if (self.calc(mid, A, B) >= k):
                right = mid
            else:
                left = mid
        return right

    def calc(self, x, A, B):
        # AB长度
        n = len(A)
        m = len(B)
        # 小于等于x的数量
        num = 0
        # 双指针上下边界
        start = 0
        end = m - 1
        while start <= n - 1:
            while end >= 0:
                if A[start] + B[end] > x:
                    end -= 1
                else:
                    break
            # 因为A[start]+B[end]<=x 所以A[start]+B[0]....A[start]+B[end-1]都小于等于x
            num += end + 1
            start += 1
        return num


# 二分 双指针 O(NlongMlogMX)
