# Description
# Given n kinds of items, and each kind of item has an infinite number available. The i-th item has size A[i] and value V[i].
# Also given a backpack with size m. What is the maximum value you can put into the backpack?

# You cannot divide item into small pieces.
# Total size of items you put into backpack can not exceed m.
# Example
# Example 1:

# Input: A = [2, 3, 5, 7], V = [1, 5, 2, 4], m = 10
# Output: 15
# Explanation: Put three item 1 (A[1] = 3, V[1] = 5) into backpack.


class Solution:
    def backPackIII(self, A, V, m):
        n = len(A)
        dp = [0] * (m + 1)        
        for i in range(n):
            for j in range(A[i], m + 1):
                dp[j] = max(dp[j], dp[j - A[i]] + V[i])      
        return dp[m]
