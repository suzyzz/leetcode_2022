# Description
# Implement pow(x, n). (n is an integer.)

# You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

# Example
# Example 1:

# Input: x = 9.88023, n = 3
# Output: 964.498
# Example 2:

# Input: x = 2.1, n = 3
# Output: 9.261
# Example 3:

# Input: x = 1, n = 0
# Output: 1
# Challenge
# O(logn) time


# 快速幂 - O(logN)

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = abs(n)
        
        if n == 0:
            return 1
        if n % 2 ==0:
            tmp = self.myPow(x, n // 2)
            return tmp * tmp
        else:
            tmp = self.myPow(x, n // 2)
            return tmp * tmp * x
            
