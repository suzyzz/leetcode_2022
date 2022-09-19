# Description
# Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

# Example
# Example 1

# Input：array = [1,2,7,8,5], k = 3
# Output：[10,17,20]
# Explanation：
# 1 + 2 + 7 = 10
# 2 + 7 + 8 = 17
# 7 + 8 + 5 = 20

# 前缀和
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if k == 0:
            return []
        n = len(nums)
        sum = [0] * n
        #计算前缀和
        for i in range(1,n):
            sum[i] = sum[i - 1] + nums[i]
        res = []
        k -= 1
        for i in range(k,n):
            res.append(sum[i] - sum[i - k] + nums[i-k])
        return res
# 滑动窗口
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if k == 0:
            return []
        n = len(nums)
        l,r,sum = 0,k - 1,0
        res = []
        # 计算初始窗口的和
        for i in range(k):
            sum += nums[i];
        res = []
        res.append(sum)
        while r < n - 1:
            sum -= nums[l]
            l += 1
            r += 1 #窗口右移
            sum += nums[r]
            res.append(sum)
        return res
