# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 104
# -104 <= nums[i] <= 104

# Method: Quick select
class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
        n = len(nums)
        # 为了方便编写代码，这里将第 k 大转换成第 k 小问题。
        k = n - k
        return self.partition(nums, 0, n - 1, k)
    
    def partition(self, nums, start, end, k):
        left, right = start, end
        pivot = nums[left]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # 如果第 k 小在右侧，搜索右边的范围，否则搜索左侧。
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        return nums[k]
        
