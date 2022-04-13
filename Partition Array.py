# Description
# Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

# All elements < k are moved to the left
# All elements >= k are moved to the right
# Return the partitioning index, i.e the first index i nums[i] >= k.

# If all elements in nums are smaller than k, then return nums.length
# 0 <= nums.length <= 20000<=nums.length<=2000

# Example
# Example 1:

# Input:

# nums = []
# k = 9
# Output:

# 0
# Explanation:

# Empty array, print 0.

# Example 2:

# Input:

# nums = [3,2,2,1]
# k = 2
# Output:

# 1
# Explanation:

# the real array is[1,2,2,3].So return 1.

# Challenge
# Can you partition the array in-place and in O(n)O(n)?

#Method: 自己写暴力解 162ms
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums, k):
        index = 0
        for i in nums:
            if i < k:
                index += 1
        return index
 
# Method: Two Pointers 122ms

# 伪代码如下：

# 令left = 0，right = length-1。
# 当nums[left] < k时，left指针向右移动。
# 当nums[right] >= k时，right指针向左移动。
# 如果left <= right，交换两个值。
# 如果left > right，返回left作为最终结果，否则返回第二步。

 class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left
