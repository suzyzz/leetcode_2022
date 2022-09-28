# Description
# Given a sorted array of n integers, find the starting and ending position of a given target value.
# If the target is not found in the array, return [-1, -1].

# Example
# Example 1:
# Input:
# array = []
# target = 9
# Output:
# [-1,-1]
# Explanation:9 is not in the array.

# Example 2:
# Input:
# array = [5, 7, 7, 8, 8, 10]
# target = 8
# Output:
# [3,4]
# Explanation:The [3,4] subinterval of the array 1 has the value 8.

# Challenge
# O(log n) time.

# 二分 - O(n+m)	一遍写出关答


class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def search_range(self, a: List[int], target: int) -> List[int]:
        if not a or not target:
            return [-1, -1]
        
        answer = self.bineary_search(a, target)
        if answer == [-1, -1]:
            return answer

        left, right = answer[0], answer[1]
        while left > 0:
            if a[left - 1] == target:
                left -= 1
            else: 
                break
        while right < len(a) - 1:
            if a[right + 1] == target:
                right += 1
            else: break

        return [left, right]

    def bineary_search(self, a, target):
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] == target:
                return [mid, mid]
            elif a[mid] < target:
                start = mid
            else:
                end = mid
        
        if a[start] == target:
            return [start, start]
        elif a[end] == target:
            return [end, end]
        return [-1, -1]
 
