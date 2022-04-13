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

# Method 1: 自己写的 fail tow pointers -timeout
class Solution:

    def two_sum6(self, nums, target):
        if not nums:
            return 0

        pairs = []
        for left in range(len(nums)):
            right = len(nums) - 1
            while left < right:
                new = [min(nums[left], nums[right]), max(nums[left], nums[right])]
                if sum(new) == target and new not in pairs:
                    pairs.append(new)
                right -= 1

        return len(pairs)
