# Description
# Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

# Example
# Example 1:

# Input: nums = [1,1,2,45,46,46], target = 47 
# Output: 2
# Explanation:

# 1 + 46 = 47
# 2 + 45 = 47
# Example 2:

# Input: nums = [1,1], target = 2 
# Output: 1
# Explanation:
# 1 + 1 = 2

# Method 1: 自己写的 fail sorted + two pointers - timeout
class Solution:

    def two_sum6(self, nums, target):
        if not nums:
            return 0

        nums_new = []
        for num in nums:
            nums_new.append(num)
            index = len(nums_new) - 1
            while index > 0 and nums_new[index - 1] > nums_new[index]:
                temp = nums_new[index - 1]
                nums_new[index - 1] = nums_new[index]
                nums_new[index] = temp
                index -= 1

        pairs = []
        for left in range(len(nums_new)):
            right = len(nums_new) - 1
            while left < right:                
                if nums_new[left] + nums_new[right] == target and [nums_new[left], nums_new[right]] not in pairs:
                    pairs.append([nums_new[left], nums_new[right]])
                right -= 1

        return len(pairs)
    
# Method 1: Sort + Two Pointer 
# 如果是sort完的list，就不用每个找了，从两边出发，不走回头路直到找到中心2，
# 可以分3种情况
#         1，2，3，..3, 4，5      targe = 6
# case 1 sum == target
#            i          j         sum = 6         => i + 1, j - 1
#              i     j  
        
#       case 1.1 i = j
#                ij  停下
        
#       case 1.2 i = i - 1 
#                 i + 1
        
#       case 1.3 j = j + 1 
#                 j - 1
        
# case 2 sum < target
#            i       j            sum = 5         => i + 1 
#              i     j  
# case 3 sum > target
#              i       j          sum = 7         => j - 1 
#              i     j 
        
class Solution:
    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        
        count = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] == target:
                count, left, right = count + 1, left + 1, right - 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        
        return count
