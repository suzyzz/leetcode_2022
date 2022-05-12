# Description
# Given an integer array, heapify it into a min-heap array.

# For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

# What is heap? What is heapify? What if there is a lot of solutions?

# Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.
# Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
# Return any of them.
# Example
# Example 1

# Input : [3,2,1,4,5]
# Output : [1,2,3,4,5]
# Explanation : return any one of the legitimate heap arrays
# Challenge
# O(n)O(n) time complexity

class Solution:
    def heapify(self, A: List[int]):
        for i in range(len(A)):
            self.siftup(A, i)

    def siftup(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            A[k], A[father] = A[father], A[k]
            k = father
            
