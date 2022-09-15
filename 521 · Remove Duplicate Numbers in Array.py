# Description
# Given an array of integers, remove the duplicate numbers in it.
# You should:

# Do it in place in the array.
# Put the element after removing the repetition at the beginning of the array.
# Return the number of elements after removing duplicate elements.
# Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)

# You don't need to keep the original order of the integers.

# Example
# Example 1:

# Input:
# nums = [1,3,1,4,4,2]
# Output:
# [1,3,4,2,?,?]
# 4
# Explanation:

# Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
# Return the number of unique integers in nums => 4.
# Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

# Example 2:

# Input:
# nums = [1,2,3]
# Output:
# [1,2,3]
# 3
# Challenge
# Do it in O(n) time complexity.
# Do it in O(nlogn) time without extra space.


# 简单的题居然没写出来- 因为被模板禁锢住了， 想法想到了 但觉得不能这么简单 结果就是这么简单？！
# 关答1 - O(n) time, O(n) space - hashmap
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        d, result = {}, 0
        for num in nums:
            if num not in d:
                d[num] = True
                nums[result] = num
                result += 1

        return result
 

# 关答2 - 。sort O(nlogn) time, O(1) extra space
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        nums.sort()
        result = 1
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1
                
        return result
