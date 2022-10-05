# Description
# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.The overall run time complexity should be O(log(m + n))O(log(m+n)).

# The definition of the median:

# The median here is equivalent to the median in the mathematical definition.
# The median is the middle of the sorted array.
# If there are n numbers in the array and n is an odd number, the median is A[(n - 1) / 2]A[(n−1)/2].
# If there are n numbers in the array and n is even, the median is A[(n - 1) / 2] + A[(n - 1) / 2 + 1]) / 2A[(n−1)/2]+A[(n−1)/2+1])/2.
# For example, the median of the array A=[1,2,3] is 2, and the median of the array A=[1,19] is 10.

# Example
# Example 1:
# Input:
# A = [1,2,3,4,5,6]
# B = [2,3,4,5]
# Output:3.5
# Explanation:The combined array is [1,2,2,3,3,4,4,5,5,6], and the median is (3 + 4) / 2.
  
# Example 2:
# Input:
# A = [1,2,3]
# B = [4,5]
# Output:3
# Explanation:The combined array is [1,2,3,4,5], and the median is 3.

# Challenge
# The overall run time complexity should be O(log (m+n))O(log(m+n)).


# 关答 二分答案 - O(log（n+m)）

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n // 2 + 1)
        else:
            smaller = self.findKth(A, 0, B, 0, n // 2)
            bigger = self.findKth(A, 0, B, 0, n // 2 + 1)
            return (smaller + bigger) / 2

    def findKth(self, A, index_a, B, index_b, k):
        if len(A) == index_a:
            return B[index_b  + k - 1]
        if len(B) == index_b:
            return A[index_a + k - 1]
        if k == 1:
            return min(A[index_a], B[index_b])
        
        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else None
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else None
        
        if b is None or (a is not None and a < b):
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
        return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)
