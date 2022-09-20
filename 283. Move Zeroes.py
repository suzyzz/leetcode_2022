# Description
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Example
# Example 1:

# Input: nums = [0, 1, 0, 3, 12],
# Output: [1, 3, 12, 0, 0].
# Example 2:

# Input: nums = [0, 0, 0, 3, 1],
# Output: [3, 1, 0, 0, 0].



# quickselect - O(n)	一遍写出 比关答少一个indent

from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def move_zeroes(self, nums: List[int]):
        if not nums:
            return 
        j = 0
        for i in range(len(nums)):          
            if nums[i] != 0:
                continue
            j = max(i + 1, j)
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j < len(nums) and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
        return
      
# 关答1
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # 将两个指针先指向数组头部
        left, right = 0, 0
        while right < len(nums):
            # 遇到非0数赋值给新数组指针指向的位置
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                #将left向后移动一位
                left += 1
            right += 1

        # 若新数组指针还未指向尾部，将剩余数组赋值为0
        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1 
            
            
#  关答2
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
