# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).


# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

# Constraints:

# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.


# Method 1: DFS, TLE
class Solution:
    def is_match(self, source, pattern):
        # 特殊情况处理
        if source == None or pattern == None:
            return False
        # DFS
        return self.is_match_helper(source, 0, pattern, 0)        
    
    # 如果从pIndex开始，p中都是*， 返回true，
    def all_star(self, pattern, p_index):
        for i in range(p_index, len(pattern)):
            if pattern[i] != '*':
                return False
        return TrueDFS

    # 如果两个字符相同，或者s为一个字符p为一个？， 那么两个字符可以匹配，返回true
    def is_match_char(self, s_char, p_char):
        return s_char == p_char or p_char == '?'

    # 递归的定义
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀能 return True
    def is_match_helper(self, source, s_index, pattern, p_index):
        # 递归的出口
        # 双双都走到底
        if p_index == len(pattern):
            return s_index == len(source)

        # 如果source剩下空，pattern剩下的 必须是空或者全部是*
        if s_index == len(source):
            return self.all_star(pattern, p_index)

        # 递归的拆解
        # 取得source和pattern当前指针指向的字母
        s_char = source[s_index]
        p_char = pattern[p_index]

        # 如果p_char 不为*，当前对应的s_char和p_char匹配 && 之后的字符串也匹配
        if p_char != '*':
            return self.is_match_char(s_char, p_char) and \
                self.is_match_helper(source, s_index + 1, pattern, p_index + 1)

        # *可以匹配source中任何前缀，继续递归之后看两个字符串余下的部分是否匹配
        for new_s_index in range(s_index, len(source) + 1):
            # 一旦有匹配，立即返回True
            if self.is_match_helper(source, new_s_index, pattern, p_index + 1):
                return True
        # 不可能匹配 返回false
        return False
        
# Method 2: improve DFS by DC
class Solution:
    def is_match(self, source, pattern):
        # 特殊情况处理
        if source == None or pattern == None:
            return False
        # DFS
        return self.is_match_helper(source, 0, pattern, 0)        
    
    # 如果从pIndex开始，p中都是*， 返回true，
    def all_star(self, pattern, p_index):
        for i in range(p_index, len(pattern)):
            if pattern[i] != '*':
                return False
        return True

    # 如果两个字符相同，或者s为一个字符p为一个？， 那么两个字符可以匹配，返回true
    def is_match_char(self, s_char, p_char):
        return s_char == p_char or p_char == '?'

    # 递归的定义
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀能 return True
    def is_match_helper(self, source, s_index, pattern, p_index):
        # 递归的出口
        # 双双都走到底
        if p_index == len(pattern):
            return s_index == len(source)

        # 如果source剩下空，pattern剩下的 必须是空或者全部是*
        if s_index == len(source):
            return self.all_star(pattern, p_index)

        # 递归的拆解
        # 取得source和pattern当前指针指向的字母
        s_char = source[s_index]
        p_char = pattern[p_index]

        # 如果p_char 不为*，当前对应的s_char和p_char匹配 && 之后的字符串也匹配
        if p_char != '*':
            return self.is_match_char(s_char, p_char) and \
                self.is_match_helper(source, s_index + 1, pattern, p_index + 1)

        # 如果p_char为*， match = 当前匹配空，之后的字符串也匹配 || 
        # 当前*匹配一个字符，之后也匹配
        return self.is_match_helper(source, s_index + 1, pattern, p_index) or \
                self.is_match_helper(source, s_index, pattern, p_index + 1)
        
    
#  Method 3: Memo
class Solution:
    def is_match(self, source, pattern):
        # 特殊情况处理
        if source == None or pattern == None:
            return False
        # 记忆
        return self.is_match_helper(source, 0, pattern, 0, {})        
    
    # 如果从pIndex开始，p中都是*， 返回true，
    def all_star(self, pattern, p_index):
        for i in range(p_index, len(pattern)):
            if pattern[i] != '*':
                return False
        return True

    # 如果两个字符相同，或者s为一个字符p为一个？， 那么两个字符可以匹配，返回true
    def is_match_char(self, s_char, p_char):
        return s_char == p_char or p_char == '?'

    # 递归的定义
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀能 return True
    def is_match_helper(self, source, s_index, pattern, p_index, memo):
        # 递归的出口
        # 双双都走到底
        if p_index == len(pattern):
            return s_index == len(source)

        # 如果source剩下空，pattern剩下的 必须是空或者全部是*
        if s_index == len(source):
            return self.all_star(pattern, p_index)
        
        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]

        # 递归的拆解
        # 取得source和pattern当前指针指向的字母
        s_char = source[s_index]
        p_char = pattern[p_index]

        match = False

        # 如果p_char 不为*，match = 当前对应的s_char和p_char匹配 && 之后的字符串也匹配
        if p_char != '*':
            match = self.is_match_char(s_char, p_char) and \
            self.is_match_helper(source, s_index + 1, pattern, p_index + 1, memo)

        # 如果p_char为*， match = 当前匹配空，之后的字符串也匹配 || 
        # 当前*匹配一个字符，之后也匹配
        else:
            match = \
            self.is_match_helper(source, s_index + 1, pattern, p_index, memo) \
            or self.is_match_helper(source, s_index, pattern, p_index + 1, memo)

        # 记录memo备用
        memo[(s_index, p_index)] = match
        return match
    
    
