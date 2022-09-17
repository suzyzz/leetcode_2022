# Description
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# Modify array A in-place to merge array B into the back of array A.

# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

# Example
# Example 1:

# Input:

# A = [1,2,3]
# m = 3
# B = [4,5]
# n = 2
# Output:

# [1,2,3,4,5]
# Explanation:

# After merge, A will be filled as [1,2,3,4,5]
# Example 2:

# Input:

# A = [1,2,5]
# m = 3
# B = [3,4]
# n = 2
# Output:

# [1,2,3,4,5]
# Explanation:

# After merge, A will be filled as [1,2,3,4,5]

# Merge Sort - O(n + m)	一遍写出关答

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        if not A or not B:
            return
        tmp = [0] * (m + n)
        a_index, b_index, tmp_index = 0, 0, 0
        while a_index < m and b_index < n:
            if  A[a_index] < B[b_index]:
                tmp[tmp_index] = A[a_index]
                tmp_index, a_index = tmp_index + 1, a_index + 1
            else:
                tmp[tmp_index] = B[b_index]
                tmp_index, b_index = tmp_index + 1, b_index + 1    
        while a_index < m:
            tmp[tmp_index] = A[a_index]
            tmp_index, a_index = tmp_index + 1, a_index + 1    
        while b_index < n:
            tmp[tmp_index] = B[b_index]
            tmp_index, b_index = tmp_index + 1, b_index + 1    

        for i in range(len(tmp)):
            A[i] = tmp[i]



