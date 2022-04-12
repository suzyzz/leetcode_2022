# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Method DP - Bottom-Up
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp           
        return one
      
# Method DP - Top-Down recursion + memoization      
class Solution(object):
    def climbStairs(self, n, memo = {}):
        if n in memo: return memo[n]
        if n == 0: return 1
        if n < 0: return 0
        
        memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return memo[n]
