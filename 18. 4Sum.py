# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109


#sum(first two) = sum(last two)
class Solution(object):
    '''
    题意：找到数列中所有和等于目标数的四元组，需去重
    多枚举一个数后，参照3Sum的做法，O(N^3)    
    '''
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res

       
       
# 自己写的错误例子 先固定n3, n4
class Solution:
    def four_sum(self, numbers: List[int], target: int) -> List[List[int]]:
        numbers.sort()
        answer = []
        print(numbers)
        for n3 in range(2, len(numbers) - 1):
            if n3 != 2 and numbers[n3] == numbers[n3 - 1]:
                continue
            for n4 in range(n3 + 1, len(numbers)):
                if n4 != n3 + 1 and numbers[n4] == numbers[n4 - 1]:
                    continue

                n1, n2 = 0, n3 - 1
                k = target - numbers[n3] - numbers[n4]
                print(n1, n2, n3, n4, k, [numbers[n1], numbers[n2], numbers[n3], numbers[n4]])
                while n1 < n2:

                    if numbers[n1] + numbers[n2] == k:
                        answer.append([numbers[n1], numbers[n2], numbers[n3], numbers[n4]])
                        n1 += 1                     
                        n2 -= 1    
                        while n1 < n2 and numbers[n1] == numbers[n1 - 1]:
                            n1 += 1
                        while n1 < n2 and numbers[n2] == numbers[n2 + 1]:
                            n2 -= 1                  
                    elif numbers[n1] + numbers[n2] < k:
                        n1 += 1                        
                    else:
                        n2 -= 1
                        
        return answer

        # for n3 in range(2, len(numbers) - 1):
        #     if n3 != 2 and numbers[n3] == numbers[n3 - 1]:
        #         continue
        #     for n4 in range(n3 + 1, len(numbers)):
        #         if n4 != n3 + 1 and numbers[n4] == numbers[n4 - 1]:
        #             continue        

# Test Data 
# [1,0,-1,-1,-1,-1,0,1,1,1,2]
# 2
# n3, n4 去重有问题
# [。。。， 1, 1, 1, 1, 2]
#         n3, n4              <= 这样就错过了让 n2 = 1 的机会
#                n3, n4       <= 应该在这里

#  先固定n3, n4的话这个问题不好避免，最好还是先固定n1, n2,
