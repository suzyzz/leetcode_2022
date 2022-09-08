# Description
# Given an array of integers that is already sorted in ascending order of absolute value, find two numbers so that the sum of them equals a specific number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Note: the subscript of the array starts with 0
# You are not allowed to sort this array.

# It is guaranteed that all numbers in the numsnums is distinct.
# The length of numsnums is \leq 100\,000≤100000.
# The number in numsnums is \leq 10^9≤10 


# Example
# Input: 
# [0,-1,2,-3,4]
# 1
# Output: 
# [[1,2],[3,4]]
# Explanation: 
# nums[1] + nums[2] = -1 + 2 = 1, nums[3] + nums[4] = -3 + 4 = 1
# You can return [[3,4],[1,2]], the system will automatically help you sort it to [[1,2],[3,4]]. But [[2,1],[3,4]] is invaild.
# Challenge
# \mathcal{O}(n)O(n) time complexity and \mathcal{O}(1)O(1) extra space


# hashmap O(n)	一遍写出关答
class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
             we will sort your return value in output
    """
    def two_sum_v_i_i(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 2:
            return []
        answer = []
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                answer.append([hash[nums[i]], i])
            else:
                hash[target - nums[i]] = i
        return answer
      
# 关答 - 同向双指针 - O(n)
class Solution:
    def two_sum_v_i_i(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if (n == 0):
            return []
        left = 0
        right = 0
        for i in range(n):
            if (nums[i] > nums[right]):
                right = i
            if (nums[i] < nums[left]):
                left = i
        ans = []
        while (nums[left] < nums[right]):
            if (nums[left] + nums[right] < target):
                left = self.nextleft(left, nums)
                if left == -1:
                    break
            elif (nums[left] + nums[right] > target):
                right = self.nextright(right, nums)
                if right == -1:
                    break
            else:
                tmp = [left, right]
                if left > right:
                    tmp[0], tmp[1] = tmp[1], tmp[0]
                ans.append(tmp)
                left = self.nextleft(left, nums)
                if left == -1:
                    break
        return ans
    def nextleft(self, left, nums):
        n = len(nums)
        if (nums[left] < 0):
            for i in range(left - 1, -1, -1):
                if (nums[i] < 0):
                    return i
            for i in range(n):
                if (nums[i] >= 0):
                    return i
            return -1
        for i in range(left + 1, n):
            if (nums[i] >= 0):
                return i
        return -1
    def nextright(self, right, nums):
        n = len(nums)
        if (nums[right] > 0):
            for i in range(right - 1, -1, -1):
                if (nums[i] > 0):
                    return i
            for i in range(n):
                if (nums[i] <= 0):
                    return i
            return -1
        for i in range(right + 1, n):
            if (nums[i] <= 0):
                return i
        return -1
