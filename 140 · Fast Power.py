# Description
# Calculate the a^n \% ba n %b where a, b and n are all 32bit non-negative integers.
# a, b and n are all 32-bit non-negative integers

# Example
# Example 1:
# Input:
# a = 3
# b = 7
# n = 5
# Output:5
# Explanation:3 ^ 5 % 7 = 5

# Example 2:
# Input:
# a = 3
# b = 1
# n = 0
# Output:0
# Explanation:3 ^ 0 % 1 = 0

# Challenge
# O(logn)O(logn) time complexity

# 快速幂 - O(logN)
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fast_power(self, a: int, b: int, n: int) -> int:
        if n == 0:
            return 1 % b
        product = self.fast_power(a, b, n//2)
        product = (product * product) % b
        if n % 2 == 1:
            product = (product * a) % b
        return product
      
# 二进制 O(logn)
    def fast_power(self, a: int, b: int, n: int) -> int:
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = a * a % b
            n = n // 2
        return ans % b
