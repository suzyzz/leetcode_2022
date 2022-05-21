# Description
# Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.
# Ignore case

# Example
# Example1
# Input:
# "CatMat"
# ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
# Output: 3
# Explanation:
# we can form 3 sentences, as follows:
# "CatMat" = "Cat" + "Mat"
# "CatMat" = "Ca" + "tM" + "at"
# "CatMat" = "C" + "at" + "Mat"
# Example1
# Input:
# "a"
# []
# Output: 
# 0

from typing import (
    Set,
)

class Solution:
    def word_break3(self, s: str, dict: Set[str]) -> int:
        if not s or not dict:
            return 0
        max_length, lower_dict = self.initialize(dict)
        #返回的是index=0的所有方案数 memo[0]
        return self.memo_search(s.lower(), 0, max_length, lower_dict, {})

    def initialize(self, dict):
        max_length, lower_dict = 0, set()
        for word in dict:
            max_length = max(max_length, len(word))
            lower_dict.add(word.lower())
        return max_length, lower_dict
    
    # 递归的定义： 从index开始的后缀字符串s[index..]可以划分为dict里的单词组合的方案数
    def memo_search(self, s, index, max_length, lower_dict, memo):
        # 递归的出口：已经划分到s的末尾 返回1
        if index == len(s):
            return 1
        # 记忆化搜索：如果s[index..]处理过，直接返回结果：这个分支下面的总数
        if index in memo:
            return memo[index]
        # s[index..]这个分支下面的方案总数
        result = 0
        # 递归的拆解：枚举下一个划分的字符串重点，分治解决每个子问题
        for end in range(index + 1, len(s) + 1):
            # 剪枝：如果超过长度结束
            if end - index > max_length:
                break
            # 枚举的结果
            word = s[index: end]
            # 如果不在dict里继续下个枚举
            if word not in lower_dict:
                continue
            # 如果在dict里，从end开始继续划分，后面的方案数要加总到当前方案数里
            result += self.memo_search(s, end, max_length, lower_dict, memo)
        # 记录当前index对应的方案数
        memo[index] = result
        # 返回结果给上次
        return memo[index]
