# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

# Method: Binary Search + opposite two pointers
class Solution:
    def k_closest_numbers(self, a, target, k):
        right = self.findUpperClosest(a, target)
        left = right - 1

        results = []
        for _ in range(k):
            if self.isLeftCloser(a, target, left, right):
                results.append(a[left])
                left -= 1
            else:
                results.append(a[right])
                right += 1
        return results

    def isLeftCloser(self, a, target, left, right):
        if left < 0:
            return False
        if right >= len(a):
            return True
        return target - a[left] <= a[right] - target
    
    def findUpperClosest(self, a, target):
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] >= target:
                end = mid
            else:
                start = mid
            
        if a[start] >= target:
            return start
        if a[end] >= target:
            return end
        return len(a)


        
