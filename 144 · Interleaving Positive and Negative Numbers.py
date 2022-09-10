# Description
# Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.
# You are not necessary to keep the original order of positive integers or negative integers.

# Example
# Example 1

# Input : [-1, -2, -3, 4, 5, 6]
# Outout : [-1, 5, -2, 4, -3, 6]
# Explanation :  any other reasonable answer.

# 关答 partition 模板 + 相向指针排列


from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, A: List[int]):
        pos, neg = 0, 0
        for num in A:
            if num > 0:
                pos += 1
            else:
                neg += 1
        
        self.partition(A, pos > neg)
        self.interleave(A, pos == neg)
            
    def partition(self, A, start_positive):
        flag = 1 if start_positive else -1
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] * flag > 0:
                left += 1
            while left <= right and A[right] * flag < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
    
    def interleave(self, A, has_same_length):
        left, right = 1, len(A) - 1
        if has_same_length:
            right = len(A) - 2
            
        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2
