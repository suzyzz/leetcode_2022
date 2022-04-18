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
    def triangleCount(self, S):
        S.sort()
        
        ans = 0
        for i in range(len(S)):
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans
      
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
