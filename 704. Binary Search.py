# Description
# Find any position of a target number in a sorted array. Return -1 if target does not exist.

# Example
# Example 1:

# Input: nums = [1,2,2,4,5,5], target = 2
# Output: 1 or 2
# Example 2:

# Input: nums = [1,2,2,4,5,5], target = 6
# Output: -1
# Challenge
# O(logn) time

# Method 1: Recursive
class Solution:
    def findPosition(self, nums, target):
        if not nums or target == None:
            return -1

        return self.binarysearch(nums, target, 0, len(nums) - 1)

    def binarysearch(self, nums, target, start, end):
        if start > end:
            return -1

        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binarysearch(nums, target, mid + 1, end)
        return self.binarysearch(nums, target, start, mid - 1)
      
# Method 2: Binary Search      
class Solution(object):
    def findPosition(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (r + l) / 2
            if (nums[m] == target):
                return m
            elif (nums[m] > target):
                r = m - 1
            else:
                l = m + 1
        return -1
