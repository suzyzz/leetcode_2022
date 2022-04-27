# Description
# Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?

# Example
# Example 1:

# Input: [3, 4, 6, 7]
# Output: 3
# Explanation:
# They are (3, 4, 6), 
#          (3, 6, 7),
#          (4, 6, 7)
# Example 2:

# Input: [4, 4, 4, 4]
# Output: 4
# Explanation:
# Any three numbers can form a triangle. 
# So the answer is C(3, 4) = 4

# Method: Two pointer 相向双指针, fix largest edge
class Solution:
    def triangleCount(self, s: List[int]) -> int:
        s.sort()
        count = 0
        for large in range(2, len(s)):
            small, mid = 0, large - 1
            while small < mid:
                if s[small] + s[mid] > s[large]:
                    count += (mid - small)
                    mid -= 1
                else:
                    small += 1
        return count
      
# Method: Two pointer 同向双指针, fix smallest edge
import bisect
class SolutionBisect:

    def triangleCount(self, nums):
        
        nums.sort()
        
        total = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                k = bisect.bisect_left(nums, nums[i] + nums[j], j+1)
                total += k - (j+1)
                    
        return total
    
    
# 自己写的while if没用对 太慢能过
class Solution:
    def triangle_count(self, s: List[int]) -> int:
        s.sort()
        count = 0
        for large in range(len(s)):
            small, mid = 0, large - 1
            while small < mid:
                while small < mid and s[small] + s[mid] <= s[large]:
                    small += 1
                while small < mid and s[small] + s[mid] > s[large]:
                    count += (mid - small)
                    mid -= 1
        return count
