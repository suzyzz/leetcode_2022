# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105


# Method 1: DP
class Solution:
    def can_jump(self, a: List[int]) -> bool:
        if not a:
            return False

        n = len(a)
        dp = [False] * n

        dp[0] = True

        for i in range(1, n):
            for j in range(i):
                if dp[j] and j + a[j] >= i:
                    dp[i] = True
                    break
        return dp[n - 1] 
      
      
      
# Method 2: Greedy
class Solution:
    def can_jump(self, arr):
        res, length = 0, len(arr)
        if length == 0:							  # 剪枝提前判断输出
            return  False
        elif length == 1:
            return True
            
        for index in range(length):
            if index <= res:					   #可以跳到index处，则判断并更新最大值信息
                res = max(res, index + arr[index])
            else:
                return False	                   #说明无法跳到index位置，肯定不能到最后位置，所以直接False
        return res >= length - 1  
