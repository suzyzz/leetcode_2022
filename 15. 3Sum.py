# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


# 自己写的 timeout
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def three_sum(self, numbers):
        # write your code here
        output = []
        target = 0
        while target < len(numbers):
            left = target + 1
            while left < len(numbers) - 1:
                for right in range(left + 1, len(numbers)):
                    new = [numbers[target], numbers[left], numbers[right]]
                    new.sort()
                    if numbers[left] + numbers[right] == 0 - numbers[target] and new not in output:
                        output.append(new)
                    right += 1
                left += 1
            target += 1
        return output
      
# 正确的暴力解 用 if target-nums[j] in dict 来代替 第三个loop
class Solution:
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []
        result = []
        for i in range(len(nums)-2):
            target = - nums[i]
            dict = {}
            for j in range(i+1,len(nums)):
                if target-nums[j] in dict:
                    res = sorted([nums[i],nums[j],target-nums[j]])
                    if res not in result:
                        result.append(res)
                else:
                    dict[nums[j]] = j
        return result
