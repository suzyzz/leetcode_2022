# same as 608
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
  
# Method: 自己写Two Pointer 过了 
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers, target):
        # write your code here
        if not numbers:
            return [-1, -1]
        left = 0
        right = 1
        while left < right:
            while right < len(numbers):
                if target == numbers[left] + numbers[right]:
                    return [left, right]
                right += 1
            left += 1
            right = left + 1
        return [-1, -1]
  
  
#   算法：sort + 双指针
# 先对数组拷贝

# 然后对数组排序，在排序后的数组中利用双指针从左右向中间寻找

# 如果numbers[i] + numbers [j] == target 说明找到答案
# 如果numbers[i] + numbers [j] < target 说明当前和比答案小。左指针右移
# 如果numbers[i] + numbers [j] > target 说明当前和比答案大。右指针左移
# 然后在拷贝数组中找到对应numbers[i]和numbers[j] 的下标，对这两个下标排个序
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if not numbers:
            return [-1, -1]
        
        # transform numbers to a sorted array with index
        nums = [
            (number, index)
            for index, number in enumerate(numbers)
        ]
        nums = sorted(nums)
        
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] > target:
                right -= 1
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                return sorted([nums[left][1], nums[right][1]])
        
        return [-1, -1]
      
#hashmap - Best 找第一遍存起来，然后找第二遍 target - nums[i] 看在不在之前存过的地方
class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        
        return [-1, -1]
      
      
# numbers = [2,7,11,15]
# target = 9
# i hash      target - nums[i]    in hash?    hash[nums[i]] = i       return [hash[target - nums[i]], i]
# 0 {}        9 - 2 = 7           No          {2: 0}
# 1 {2: 0}    9 - 7 = 2           Yes                                 return [hash[2] = 0, 1]


# numbers = [15,2,7,11]
# target = 9
# i hash              target - nums[i]    in hash?    hash[nums[i]] = i       return [hash[target - nums[i]], i]
# 0 {}                9 - 15 = -2         No          {15: 0}
# 1 {15: 0}           9 - 2 = 7           No          {2: 1}                               
# 2 {15: 0, 2: 1}     9 - 7 = 2           Yes                                 return [hash[2] = 1, 2]
