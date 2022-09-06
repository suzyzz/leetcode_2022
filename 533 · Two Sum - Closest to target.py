# Description
# Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

# Return the absolute value of difference between the sum of the two numbers and the target.

# Example
# Example1
# Input:  nums = [-1, 2, 1, -4] and target = 4
# Output: 1
# Explanation:
# The minimum difference is 1. (4 - (2 + 1) = 1).
# Example2

# Input:  nums = [-1, -1, -1, -4] and target = 4
# Output: 6
# Explanation:
# The minimum difference is 6. (4 - (- 1 - 1) = 6).
# Challenge
# Do it in O(nlogn) time complexity.
# 
# twosum - O(nlogn)	一遍写出关答

from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def two_sum_closest(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        diff = float('inf')
        while left < right:
            current_sum = nums[left] + nums[right]
            current_diff = abs(target - current_sum)
            if current_diff == 0:
                return 0
            if current_diff < diff:
                diff = current_diff
            if current_sum > target:
                right -= 1
            else:
                left += 1
        return diff



                
