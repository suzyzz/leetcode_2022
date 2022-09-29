# Description
# Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

# Example
# Example1:

# Input: [1, 3, 3, 4, 5] and target = 3, 
# Output: 2.
# Example2:

# Input: [2, 2, 3, 4, 6] and target = 4, 
# Output: 1.
# Example3:

# Input: [1, 2, 3, 4, 5] and target = 6, 
# Output: 0.
# Challenge
# Time complexity in O(logn)

# 两个二分法 - O{logn)


class Solution:
    """
    @param a: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def total_occurrence(self, a: List[int], target: int) -> int:
        first = self.bineary_search_first(a, target)
        last = self.bineary_search_last(a, target)

        if first < 0:
            return 0
        return last - first + 1
    
    def bineary_search_first(self, a, target):
        if not a:
            return  -1
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] < target:
                start = mid
            else:
                end = mid
        if a[start] == target:
            return start
        elif a[end] == target:
            return end
        else:
            return -1
        
    def bineary_search_last(self, a, target):
        if not a:
            return  -1
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] <= target:
                start = mid
            else:
                end = mid
        if a[end] == target:
            return end
        elif a[start] == target:
            return start
        else:
            return -1
        
        
