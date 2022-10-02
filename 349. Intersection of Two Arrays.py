# Description
# Given two arrays, write a function to compute their intersection.
# Each element in the result must be unique.

# Example
# Example 1:

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2], 
# Output: [2].
# Example 2:

# Input: nums1 = [1, 2], nums2 = [2], 
# Output: [2].
# Challenge
# Can you implement it in three different algorithms?

# Method 1 : hashmap O(n)	一遍写出关答

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        n2 = set(nums2)
        ans = set()
        for i in nums1:
            if i in n2 and i not in ans:
                ans.add(i)
        return list(ans)

    
# Method 2: 双指针-同向O(n+m)	一遍写出关答  
      
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()
        
        n1, n2 = len(nums1), len(nums2)
        index_1, index_2, ans = 0, 0, []
        while index_1 < n1 and index_2 < n2:
            while index_1 + 1 < n1 and nums1[index_1] == nums1[index_1 - 1]:
                index_1 += 1
            while index_2 + 1 < n2 and nums2[index_2] == nums2[index_2 - 1]:
                index_2 += 1    
            if nums1[index_1] == nums2[index_2]:
                if ans == [] or ans[-1] != nums1[index_1]:
                    ans.append(nums1[index_1])
                index_1 += 1
                index_2 += 1
            elif nums1[index_1] > nums2[index_2]:
                index_2 += 1
            else:
                index_1 += 1
        return ans
            
