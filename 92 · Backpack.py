# Description
# Given n items with size A_{i}A i an integer m denotes the size of a backpack. How full you can fill this backpack?
# (Each item can only be selected once and the size of the item is a positive integer)

# Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)

# You can not divide any item into small pieces.
# n \lt 1000n<1000
# m \lt 1e9m<1e9
# Example
# Example 1:
# Input:
# array = [3,4,8,5]
# backpack size = 10
# Output:
# 9
# Explanation:
# Load 4 and 5.


# Method 1: DP with true/false state function
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, A: List[int]) -> int:
        n = len(A)
        # state dp[i][j] 表示前 i 个数里挑若干个数是否能组成和为 j 
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        # function
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        for i in range(m, -1, -1):
            if dp[n][i]:
                return i
        return -1

#   Method 2: DP with max state function
class Solution:
    def back_pack(self, m: int, A: List[int]) -> int:
        n = len(A)
        # state dp[i][j] 表示前 i 个数能否凑出的 <=j 的最大和是多少 
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # function
        for i in range(1, n + 1):
            for j in range(0, m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[n][m]
      
#   Method 3: DP with max state function (1D) 滚动数组优化
class Solution:
    def backPack(self, m, A):
        # 如果背包容量或者物品数量为0，则直接返回
        if m == 0 or len(A) == 0:
            return 0
            
        dp = [0 for _ in range(m + 1)]
        for i in range(len(A)):
            # 滚动数组优化 倒序枚举j
            for j in range(m, A[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - A[i]] + A[i])
                
        return dp[m]

# Method 4:DFS
# Mtehod 5: 区间合并
