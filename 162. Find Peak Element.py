# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

# Method: 自己写的binary能过
class Solution:
    def find_peak(self, a):
        # write your code here
        start = 0
        end = len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] > a[mid-1] and a[mid] > a[mid+1]:
                return mid
            elif a[start] <= a[start + 1] and a[mid - 1] < a[mid]:
                start = mid
            else:
                end = mid
             
           
#Method: 关答，考虑边界效应，更简洁合理         
class Solution:
    def findPeak(self, A):
        start, end = 1, len(A) - 2
        while start + 1 <  end:
            mid = (start + end) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                return mid

        if A[start] < A[end]:
            return end
        else:
            return start
  
