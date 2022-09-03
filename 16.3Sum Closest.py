# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:
  
# Input: nums = [0,0,0], target = 1
# Output: 0
 
# Constraints:

# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


# 暴力3loop - 自己写的O(n^3)
   def three_sum_closest(self, numbers: List[int], target: int) -> int:
        if len(numbers) < 3:
            return None
        numbers.sort()
        min = float('inf')
        answer = float('inf')
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, len(numbers) - 1):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                for k in range(j + 1, len(numbers)):
                    if k > j + 1 and numbers[k] == numbers[k - 1]:
                        continue
                    sol = numbers[i] + numbers[j] + numbers[k] 
                    if abs(target - sol) < min:
                        min = abs(target - sol)
                        answer = sol
        return answer
      
