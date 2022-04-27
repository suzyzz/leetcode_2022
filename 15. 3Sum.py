# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


# 自己写的 timeout
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def three_sum(self, numbers):
        # write your code here
        output = []
        target = 0
        while target < len(numbers):
            left = target + 1
            while left < len(numbers) - 1:
                for right in range(left + 1, len(numbers)):
                    new = [numbers[target], numbers[left], numbers[right]]
                    new.sort()
                    if numbers[left] + numbers[right] == 0 - numbers[target] and new not in output:
                        output.append(new)
                    right += 1
                left += 1
            target += 1
        return output
      
# 正确的暴力解 用 if target-nums[j] in dict 来代替 第三个loop
class Solution:
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []
        result = []
        for i in range(len(nums)-2):
            target = - nums[i]
            dict = {}
            for j in range(i+1,len(nums)):
                if target-nums[j] in dict:
                    res = sorted([nums[i],nums[j],target-nums[j]])
                    if res not in result:
                        result.append(res)
                else:
                    dict[nums[j]] = j
        return result

#two sum       
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        nums = sorted(nums)
        
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, len(nums) - 1, -nums[i], results)
            
        return results

    def find_two_sum(self, nums, left, right, target, results):
        last_pair = None
        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != last_pair:
                    results.append([-target, nums[left], nums[right]])
                last_pair = (nums[left], nums[right])
                right -= 1
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1   
              
 
# 自己写的 a+b = c 慢，没用到two sum skill
 class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        numbers.sort()
        left = 0
        answer = []
        while left < len(numbers) - 2:
            right = left + 1
            while right < len(numbers) - 1:
                if 0 - (numbers[left] + numbers[right]) in numbers[right + 1:]:
                    if [numbers[left], numbers[right], 0 - (numbers[left] + numbers[right])] not in answer:
                        answer.append([numbers[left], numbers[right], 0 - (numbers[left] + numbers[right])]) 
                right += 1
            left += 1
        return answer
       
 #跟two sum 一样 稍微快一些      
 class Solution:
    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers)<3: return []
        numbers = sorted(numbers) #必须先sort
        sum_list = []
        for i in range(len(numbers)-2): #第一个数 遍历所有num 无需考虑最后两个
            if i!=0 and numbers[i]==numbers[i-1]: #avoid duplicates
                continue
            j = i+1
            k = len(numbers)-1
            while j<k:
                if numbers[j]+numbers[k]+numbers[i] == 0:
                    sum_list.append([numbers[i],numbers[j],numbers[k]])
                    j += 1
                    while j<k and numbers[j]==numbers[j-1]: #avoid duplicates
                        j+=1
                elif numbers[j]+numbers[k]+numbers[i] < 0: #小于零 增大j 数值更大
                    j += 1
                else: #小于零 减小k 数值更小
                    k -=1
        return sum_list
