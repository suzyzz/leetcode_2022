# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1


# Method 1: DP
from typing import (
    List,
)

class Solution:
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        if nums is None or not nums:
            return 0
            
        # state: dp[i] 表示以第 i 个数结尾的 LIS 的长度
        # initialization: dp[0..n-1] = 1
        dp = [1] * len(nums)
        
        # function: dp[i] = max(dp[j] + 1), j < i && nums[j] < nums[i]
        # 如果j在i的前面，并且nums[j] < nums[i]， 那么j点到i点可以拼凑成上升序列
        # 在所有上升序列中找最长，就算从起点到i找最长
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # answer, 任意一个位置都可能是 LIS 的结尾  
        return max(dp)

      
# 变形，找到最长序列
class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums:
            return 0
        
        # state: dp[i] 表示从左到右跳到i的最长sequence 的长度
        
        # initialization: dp[0..n-1] = 1
        dp = [1] * len(nums)
        
        # prev[i] 代表 dp[i] 的最优值是从哪个 dp[j] 算过来的
        prev = [-1] * len(nums)
        
        # function dp[i] = max{dp[j] + 1},  j < i and nums[j] < nums[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        # answer: max(dp[0..n-1])
        longest, last = 0, -1
        for i in range(len(nums)):
            if dp[i] > longest:
                longest = dp[i]
                last = i
        
        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        print(path[::-1])
        
        return longest
