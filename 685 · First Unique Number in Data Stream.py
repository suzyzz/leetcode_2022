# Description
# Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the terminating number is not found, return -1.

# Example
# Example1

# Input: 
# [1, 2, 2, 1, 3, 4, 4, 5, 6]
# 5
# Output: 3
# Example2

# Input: 
# [1, 2, 2, 1, 3, 4, 4, 5, 6]
# 7
# Output: -1
# Example3

# Input: 
# [1, 2, 2, 1, 3, 4]
# 3
# Output: 3

#自己写的 
from typing import (
    List,
)

class Solution:
    def first_unique_number(self, nums: List[int], number: int) -> int:
        hashmap, arrived = self.build_hashmap(nums, number, False)
        if not arrived:
            
        for key, value in hashmap.items():
            if value == 1: 
                return key
        return -1

    def build_hashmap(self, nums, number, arrived):
        hashmap = {}
        for num in nums:
            if num == number:
                arrived = True
                if num in hashmap:
                    hashmap[num] += 1
                else:
                    hashmap[num] = 1
                break
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        return hashmap, arrived

#关答 更巧妙
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        if not nums:
            return -1
        
        counter = {}
        index_range = 0
        # go through the nums first time to count the occurance
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            index_range += 1 
            if num == number:
                break
        # if the above if statement was never triggered through the for loop, it means
        # that the terminating number was not found, return -1
        else: return -1
        
        # go through the nums second time to find first unique num
        for i in range(index_range):
            if counter[nums[i]] == 1:
                return nums[i]
