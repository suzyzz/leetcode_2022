# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

# Example
# Example1

# Input: "bbbab"
# Output: 4
# Explanation:
# One possible longest palindromic subsequence is "bbbb".
# Example2

# Input: "bbbbb"
# Output: 5
  
#  Method DP
# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-516-longest-palindromic-subsequence/
class Solution:
    def longest_palindrome_subseq(self, s):
        if not s:
            return 0

        is_palindrome = [[0] * len(s) for _ in range(len(s))] #设is_palindrome[i][j]表示第i到第j个字符间的最长回文序列的长度（i<=j）

        for i in range(len(s) - 1, -1, -1):
            is_palindrome[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    is_palindrome[i][j] = is_palindrome[i + 1][j - 1] + 2
                else:
                    is_palindrome[i][j] = max(is_palindrome[i + 1][j], is_palindrome[i][j - 1])

        return is_palindrome[0][len(s) - 1]
     
   
# [1, 2, 3, 3, 4],
# [0, 1, 2, 2, 3],
# [0, 0, 1, 1, 3],
# [0, 0, 0, 1, 1],
# [0, 0, 0, 0, 1]

# [1, bb, bbb, bbba, bbbab],
# [0, 1, bb, bba, bbab],
# [0, 0, 1, ba, bab],
# [0, 0, 0, 1, ab],
# [0, 0, 0, 0, 1]
