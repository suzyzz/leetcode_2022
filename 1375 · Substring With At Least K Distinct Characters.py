# Description
# Given a string S with only lowercase characters.
# Return the number of substrings that contains at least k distinct characters.

# 10 ≤ length(S) ≤ 1,000,00010≤length(S)≤1,000,000
# 1 ≤ k ≤ 261≤k≤26
# Example
# Example 1:

# Input: S = "abcabcabca", k = 4
# Output: 0
# Explanation: There are only three distinct characters in the string.
# Example 2:

# Input: S = "abcabcabcabc", k = 3
# Output: 55
# Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
#     For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
#     There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
#     ...
#     There is 1 substring whose length is 12, "abcabcabcabc"
#     So the answer is 1 + 2 + ... + 10 = 55.



# 同向双指针-O(n)	想的没问题 差一点就写对了

class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def k_distinct_characters(self, s: str, k: int) -> int:
        if len(s) < k or k < 1:
            return 0
        i, j, ans, count = 0, 0, 0, {}
        for i in range(len(s) - k + 1):
            while j < len(s) and len(count) < k:
                count[s[j]] = count.get(s[j], 0) + 1
                j += 1
            if len(count) == k:
                ans += len(s) - j + 1
            if j > len(s):
                break
            if count[s[i]] > 1:
                count[s[i]] -= 1
            else:
                del count[s[i]]
        return ans
