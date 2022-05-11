# Description
# Given a string, find all permutations of it without duplicates.

# Example
# Example 1:

# Input:
# s = "abb"
# Output:
# ["abb", "bab", "bba"]
# Explanation:
# There are six kinds of full arrangement of abb, among which there are three kinds after removing duplicates.

# Example 2:

# Input:
# s = "aabb"
# Output:
# ["aabb", "abab", "baba", "bbaa", "abba", "baab"]


#关答
class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        chars = sorted(list(str))
        visited = [False] * len(chars)
        permutations = []
        self.dfs(chars, visited, [], permutations) 
        return permutations

    # 递归的定义: 找到所有 permutation 开头的排列
    def dfs(self, chars, visited, permutation, permutations):
        # 递归的出口：当我找到一个完整的排列
        if len(chars) == len(permutation):
            permutations.append(''.join(permutation))
            return    
        
        # 递归的拆解：基于当前的前缀，下一个字符放啥
        for i in range(len(chars)):
            # 同一个位置上的字符用过不能在用
            if visited[i]:
                continue
            # 去重：不同位置的同样的字符，必须按照顺序用。
            # a' a" b
            # => a' a" b => √
            # => a" a' b => x
            # 不能跳过一个a选下一个a
            if i > 0 and chars[i] == chars[i - 1] and not visited[i - 1]:
                continue

            # make changes
            visited[i] = True
            permutation.append(chars[i])

            # 找到所有 permutation 开头的排列
            # 找到所有 "a" 开头的
            self.dfs(chars, visited, permutation, permutations)

            # backtracking
            permutation.pop()
            visited[i] = False
