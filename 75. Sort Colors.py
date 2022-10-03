# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


# Method 1: 一次partion
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        left = 0 
        right = len(nums) - 1
        mid = left
    
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            else:
                mid += 1
# 两次partition		
    def sortColors(self, nums):
        start = self.pivot_partition(nums, 1, 0)
        self.pivot_partition(nums, 2, start)
        
    def pivot_partition(self, nums, pivot, start):      
        l, r = start, len(nums) - 1
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] >= pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                
        return l
# 暴力统计个数		
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return []

        color_cnt = [0] * 3
        for i in nums:
            color_cnt[i] += 1
        
        index = 0
        for i in range(len(color_cnt)):
            cnt = color_cnt[i]
            while cnt > 0:
                nums[index] = i
                cnt -= 1
                index += 1
