# Given a pattern and a string s, return true if s matches the pattern.
# A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

# Example 1:

# Input: pattern = "abab", s = "redblueredblue"
# Output: true
# Explanation: One possible mapping is as follows:
# 'a' -> "red"
# 'b' -> "blue"
# Example 2:

# Input: pattern = "aaaa", s = "asdasdasdasd"
# Output: true
# Explanation: One possible mapping is as follows:
# 'a' -> "asd"
# Example 3:

# Input: pattern = "aabb", s = "xyzabcxzyabc"
# Output: false
 

# Constraints:

# 1 <= pattern.length, s.length <= 20
# pattern and s consist of only lowercase English letters.

# method: DFS
class Solution:
    def wordPatternMatch(self, pattern, string):
        return self.is_match(pattern, string, {}, set())
      
    def is_match(self, pattern, string, mapping, used):
        if not pattern:
            return not string
            
        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not string.startswith(word):
                return False
            return self.is_match(pattern[1:], string[len(word):], mapping, used)
            
        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:
                continue
            
            used.add(word)
            mapping[char] = word
            
            if self.is_match(pattern[1:], string[i + 1:], mapping, used):
                return True
            
            del mapping[char]
            used.remove(word)
            
        return False


       
class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, string):
        return self.is_match(pattern, string, {}, set())

    # 递归三要素一：定义
    def is_match(self, pattern, string, mapping, used):
        # 递归三要素三：出口
        # 如果pattern结束，那么string也必须结束，才能匹配
        if not pattern:
            return not string
            
        # 取出pattern的首字母
        char = pattern[0]
        
        # 如果pattern首字母char已经有对应的字符串
        if char in mapping:
            # 首字符chart对应的字符串
            word = mapping[char]
            # 如果word不是string的前缀，则违反之前的mapping，返回false
            if not string.startswith(word):
                return False
            # 如果word是string的前缀，继续递归探求
            # pattern[1:] 和 string[len(word):]是否可以匹配
            return self.is_match(pattern[1:], string[len(word):], mapping, used)
            
        # 递归三要素二：拆解
        # 如果pattern首字母还没有对应的字符串，那么pattern首字母可能对应任何一个string的前缀
        for i in range(len(string)):
            # 取string的前缀
            word = string[:i + 1]
            
            # 如果这个字符串已经被用过，那么跳过（符合一一对应的原则）
            if word in used:
                continue
            
            # 把word标记为用过
            used.add(word)
            # 把char => word映射记录下来备用
            mapping[char] = word
            
            # 继续递归求pattern[1:] 和 string[len(word):]是否可以匹配
            if self.is_match(pattern[1:], string[i + 1:], mapping, used):
                return True
            
            # 回溯
            del mapping[char]
            used.remove(word)
            
        return False
