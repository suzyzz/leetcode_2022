# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.

# Example 1:
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

# Constraints:
# 1 <= n <= 1690

import heapq

class Solution:
    def nthUglyNumber(self, n):
        heap = []
        heapq.heappush(heap, 1)

        seen = set()
        seen.add(1)

        factors = [2, 3, 5]
        curr_ugly = 1
        
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            for f in factors:
                new_ugly = curr_ugly * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return curr_ugly
