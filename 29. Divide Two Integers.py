# Description
# Divide two integers without using multiplication, division and mod operator.
# If it will overflow(exceeding 32-bit signed integer representation range), return 2147483647
# The integer division should truncate toward zero.

# Example
# Example 1:

# Input: dividend = 0, divisor = 1
# Output: 0
# Example 2:

# Input: dividend = 100, divisor = 9
# Output: 11

# 二分-倍增 O(log(dividend/divisor))
class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend: int, divisor: int) -> int:
        # write your code here
        is_negative = False
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            is_negative = True
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        ans = 0

        while dividend >= divisor:
            
            temp = divisor
            cnt = 1
            while dividend >= temp:
                # print(temp, cnt)
                dividend -= temp
                ans += cnt
                cnt <<= 1
                temp <<= 1

        if is_negative:
            ans = -ans
        if ans > 2147483647:
            return 2147483647

        return ans
