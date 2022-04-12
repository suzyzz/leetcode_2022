# Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.)

# Method 1: Bruce Force O(n^3)
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
                   
        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                if self.is_palindrome(s, i, i + length - 1):
                    return s[i: i + length]
		
        return ""
	
    def is_palindrome(self, s, left, right):
	    while left < right and s[left] == s[right]:
		    left += 1
		    right -= 1

	    return left >= right
          

# Method 2: 中心点枚举法 enumeration O(n^2)		
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # 重点1：任何代码都要进行异常检测
        if not s:
            return ""
        
        # 重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分，属于高端代码风格技巧
        longest = ""
        for middle in range(len(s)):
            # 重点3：子函数化避免重复代码
            sub = self.find_palindrome_from(s, middle, middle)
	        # 重点4：通过返回值来避免使用全局变量这种不好的代码风格
            if len(sub) > len(longest):
                longest = sub
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub
                
		# 重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分，属于高端代码风格技巧
        return longest
        
    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string):
            # 重点5：将复杂判断拆分到 while 循环内部，而不是放在 while 循环中，提高代码可读性
            if string[left] != string[right]:
                break
            left -= 1
            right += 1
            
        return string[left + 1:right]
	

# Method 3: DP O(n^2)	
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
            
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i - 1] = True
            
        longest, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j] and length + 1 > longest:
                    longest = length + 1
                    start, end = i, j
                    
        return s[start:end + 1]	
	
	
	
	
	
	
# check 2: 中心点枚举法 enumeration		
# class Solution:
#     def longestPalindrome(self, s):
#         if not s:
#             return ""

#         answer = (0, 0)
#         for mid in range(len(s)):
#             print('\n*****   mid for loop', 'mid', mid, 'answer', answer, 's[mid]', s[mid])
#             answer = max(answer, self.get_palindrom_from(s, mid, mid))
#             # print(2, 'mid', mid, 'answer', answer, s[answer[1]: answer[0] + answer[1]])
#             answer = max(answer, self.get_palindrom_from(s, mid, mid + 1))
#             # print(3, 'mid', mid, 'answer', answer, s[answer[1]: answer[0] + answer[1]])

#         return s[answer[1]: answer[0] + answer[1]]

#     def get_palindrom_from(self, s, left, right):
#         print('**check', left, right)
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             print('     while is true', left, right, s[left] ,s[right])
#             left -= 1
#             right += 1
#         print('     while is false', left, right)
#         return (right - left - 1, left + 1)

# sol = Solution()
# s="abcdzdcab"
# print(sol.longestPalindrome(s=s))

# *****   mid for loop mid 0 answer (0, 0) s[mid] a
# **check 0 0
#      while is true 0 0 a a
#      while is false -1 1
# **check 0 1
#      while is false 0 1

# *****   mid for loop mid 1 answer (1, 0) s[mid] b
# **check 1 1
#      while is true 1 1 b b
#      while is false 0 2
# **check 1 2
#      while is false 1 2

# *****   mid for loop mid 2 answer (1, 1) s[mid] c
# **check 2 2
#      while is true 2 2 c c
#      while is false 1 3
# **check 2 3
#      while is false 2 3

# *****   mid for loop mid 3 answer (1, 2) s[mid] d
# **check 3 3
#      while is true 3 3 d d
#      while is false 2 4
# **check 3 4
#      while is false 3 4

# *****   mid for loop mid 4 answer (1, 3) s[mid] z
# **check 4 4
#      while is true 4 4 z z
#      while is true 3 5 d d
#      while is true 2 6 c c
#      while is false 1 7
# **check 4 5
#      while is false 4 5

# *****   mid for loop mid 5 answer (5, 2) s[mid] d
# **check 5 5
#      while is true 5 5 d d
#      while is false 4 6
# **check 5 6
#      while is false 5 6

# *****   mid for loop mid 6 answer (5, 2) s[mid] c
# **check 6 6
#      while is true 6 6 c c
#      while is false 5 7
# **check 6 7
#      while is false 6 7

# *****   mid for loop mid 7 answer (5, 2) s[mid] a
# **check 7 7
#      while is true 7 7 a a
#      while is false 6 8
# **check 7 8
#      while is false 7 8

# *****   mid for loop mid 8 answer (5, 2) s[mid] b
# **check 8 8
#      while is true 8 8 b b
#      while is false 7 9
# **check 8 9
#      while is false 8 9
# cdzdc
# [Finished in 0.3s]




#DP checks
# 1 [     [False, False, False, False, False],
#         [False, False, False, False, False],
#         [False, False, False, False, False],
#         [False, False, False, False, False],
#         [False, False, False, False, False]]

# 2 [     [True, False, False, False, False],
#         [True, True, False, False, False],
#         [False, True, True, False, False],
#         [False, False, True, True, False],
#         [False, False, False, True, True]]

# length 1
# 0 1
# 1 2
# 2 3
# 3 4
# length 2
# 0 2
# 1 3
# 2 4
# length 3
# 0 3
# 1 4
# length 4
# 0 4

# 3 [     [True, False, False, False, False],
#         [True, True, False, True, False],
#         [False, True, True, False, False],
#         [False, False, True, True, False],
#         [False, False, False, True, True]]
