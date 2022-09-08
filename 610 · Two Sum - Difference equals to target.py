# Description
# Given an sorted array of integers, find two numbers that their difference equals to a target value.
# Return a list with two number like [num1, num2] that the difference of num1 and num2 equals to target value, and num1 is less than num2.

# It's guaranteed there is only one available solution.
# Note: Requires O(1) space complexity to comple

# Example
# Example 1:

# Input: nums = [2, 7, 15, 24], target = 5 
# Output: [2, 7] 
# Explanation:
# (7 - 2 = 5)
# Example 2:

# Input: nums = [1, 1], target = 0
# Output: [1, 1] 
# Explanation:
# (1 - 1 = 0)

# 自己写的hash - 能过 但是空间超
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        target = abs(target)
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]], nums[i]]
            else:
                hash[target + nums[i]] = nums[i]
        return []
      
# 关答-同向双指针
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        target = abs(target) # 让target为正数
        j = 0
        for i in range(len(nums)):
            j = max(i + 1,j)
            print(i, j)
            while j < len(nums) and nums[j] - nums[i] < target:
                j += 1 # 指针右移到num[j]>=num[i]
            if j > len(nums):
                break # 防止指针越界
            if nums[j] - nums[i] == target: # 找到答案
                return [nums[i],nums[j]]
        return [-1,-1]
