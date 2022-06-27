# Description
# There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item.
# What's the maximum value can you put into the backpack?

# A[i], V[i], n, m are all integers.
# You can not split an item.
# The sum size of the items you want to put into backpack can not exceed m.
# Each item can only be picked up once
# m <= 1000m<=1000\
# len(A),len(V)<=100len(A),len(V)<=100

# Example
# Example 1:
# Input:
# m = 10
# A = [2, 3, 5, 7]
# V = [1, 5, 2, 4]
# Output:
# 9
# Explanation:

# Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9

# Method 1: DP 滚动数组
class Solution:
    def back_pack_i_i(self, m: int, A: List[int], V: List[int]) -> int:
        dp = [0 for i in range(m+1)]
        n = len(A)
        for i in range(n):
            for j in range(m, A[i]-1, -1):
                dp[j] = max(dp[j] , dp[j-A[i]] + V[i])
        return dp[m]
