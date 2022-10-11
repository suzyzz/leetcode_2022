# Description
# Prime factorize a given integer.
# You should sort the factors in ascending order.

# Example
# Example 1:

# Input: 10
# Output: [2, 5]
# Example 2:

# Input: 660
# Output: [2, 2, 3, 5, 11]

# 分解质因数- O(√n)

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def prime_factorization(self, num: int) -> List[int]:
        result = []
        up = int(math.sqrt(num))

        k = 2
        while k <= up and num > 1:
            while num % k == 0:
                num //= k
                result.append(k)
            k += 1
        if num > 1:
            result.append(num)
        return result
