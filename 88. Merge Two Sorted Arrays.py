
# Description
# Merge two given sorted ascending integer array A and B into a new sorted integer array.

# Example
# Example 1:

# Input:

# A = [1]
# B = [1]
# Output:

# [1,1]
# Explanation:

# return array merged.

# Example 2:

# Input:

# A = [1,2,3,4]
# B = [2,4,5,6]
# Output:

# [1,2,2,3,4,4,5,6]

#自己写的two pointer 
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        i, j = 0, 0
        C = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        while i < len(A):
            C.append(A[i])
            i += 1
        while j < len(B):
            C.append(B[j])
            j += 1
            
        return C
