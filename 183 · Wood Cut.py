# Description
# Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

# The unit of length is centimeter.The length of the woods are all positive integers,you couldn't cut wood into float length.If you couldn't get >= k pieces, return 0.

# Example
# Example 1

# Input:
# L = [232, 124, 456]
# k = 7
# Output: 114
# Explanation: We can cut it into 7 pieces if any piece is 114 long, however we can't cut it into 7 pieces if any piece is 115 long.
# And for the 124 logs, the excess can be discarded and not used in its entirety.
# Example 2

# Input:
# L = [1, 2, 3]
# k = 7
# Output: 0
# Explanation: It is obvious we can't make it.
# Challenge
# O(n log Len), where Len is the longest length of the wood.


#Method: Binary search in valid answers
class Solution:
    def woodCut(self, L, k):
        if not L:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_pieces(L, mid) >= k:
                start = mid
            else:
                end = mid
                
        if self.get_pieces(L, end) >= k:
            return end
        if self.get_pieces(L, start) >= k:
            return start
            
        return 0
        
    def get_pieces(self, L, length):
        pieces = 0
        for l in L:
            pieces += l // length
        return pieces
