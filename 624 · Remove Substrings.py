# Description
# Given a string s and a list of strings dict, do the following repeatedly for s until none of the strings in dict are substrings of s.
# If a string in dict is a substring of s, remove that substring from s
# If more than one string in dict is a substring of s, remove any one of the strings s
# Design a scheme that minimizes the length of the removed s and returns this minimum length.
# A substring is a part of string that deleted a prefix and a postfix.

# Example
# Example 1:
# Input:
# "ccdaabcdbb"
# ["ab","cd"]
# Output:2
# Explanation: The following operations are performed in order:
# s = "ccda[ab]cdbb", deleting "ab" starting with subscript 4 to get s = "ccdacdbb"
# s = "c[cd]acdbb", delete "cd" starting with subscript 1 to get s = "cacdbb"
# s = "ca[cd]bb", delete "cd" starting with subscript 2 to get s = "cabb"
# s = "c[ab]b", delete "ab" starting with subscript 1 to get s = "cb"
# The substring of s no longer exists in the dict, and the final length of s is 2

# Example 2:
# Input:
# "abcabd"
# ["ab","abcd"]
# Output:0
# Explanation: 
# abcabd -> abcd -> "" (length = 0)

# 单队列 -  通用模板
# 假设有n个单词，原字符串长度为m。因为长度为m的字符串，如果串中字符各不相同，则子串的个数为m(m+1)/2+1，因此最坏情况下字符串的子串是O(m^2)级别的,空间复杂度为O(m^2)；
# 最坏情况队列中的字符串个数会是O(m^2)级别的，对于每一个字符串都要对n个单词进行查找处理，查找处理的时间复杂度是此时队列中头元素的长度ln，最坏取个平均值m/2，因此时间复杂度为O(m^3n).

from typing import (
    Set,
)
import collections
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    
    def minLength(self, s, dict):
        # write your code here
        queue = collections.deque([s])
        visited = set([s])
        answer = len(s)
        while queue:
            cur_str = queue.popleft()
            answer = min(answer, len(cur_str))
            for sub_str in self.find_substrings(cur_str, dict):
                if sub_str not in visited:
                    visited.add(sub_str)
                    queue.append(sub_str)
        return answer
        
    def find_substrings(self, s, dict):
        results = []
        for word in dict:
            found = s.find(word)
            while found != -1:
                substring = s[:found] + s[found + len(word):]
                results.append(substring)
                found = s.find(word, found + 1) # searching start from found + 1
        return results
