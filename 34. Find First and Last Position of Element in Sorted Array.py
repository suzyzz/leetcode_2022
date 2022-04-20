# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
  
class Solution:
    def last_position(self, nums, target):
        # write your code here
        if not nums or target == None:
            return -1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid
            if nums[mid] < target:
                start = mid + 1
            if nums[mid] > target:
                end = mid -1
        
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        
        return -1

        
class Solution:
    def fisrt_search(self, nums, target):
        # write your code here
        if not nums or target == None:
            return -1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid
            if nums[mid] < target:
                start = mid + 1
            if nums[mid] > target:
                end = mid -1
        
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end 
                  
        return -1


            
