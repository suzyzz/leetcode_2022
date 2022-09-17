# Description
# Find the kth smallest number in an unsorted integer array (K start at 1).

# Example
# Example 1:

# Input: [3, 4, 1, 2, 5], k = 3
# Output: 3
# Example 2:

# Input: [1, 1, 1], k = 2
# Output: 1
# Challenge
# An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.

# quickselect - O(n)	一遍写出关答

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kth_smallest(self, k: int, nums: List[int]) -> int:
        k_index = k - 1
        return self.quickselect(nums, 0, len(nums) - 1, k_index)

    def quickselect(self, nums, start, end, k_index):
        if start >= end:
            return nums[start]
        left, right = start, end
        mid = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < mid:
                left += 1
            while left <= right and nums[right] > mid:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if right >= k_index:
            return self.quickselect(nums, start, right, k_index)
        elif left <= k_index:
            return self.quickselect(nums, left, end, k_index)
        else:
            return nums[right + 1]
