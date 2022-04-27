# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
 
# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

#自己写的timeout
class Solution(object):
    def validPalindrome(self, s):
        if self.isPalindrome(s, -1):
            return True
        for i in range(len(s)):
            if self.isPalindrome(s, i):
                return True
        return False

    def isPalindrome(self, s, index):
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and left == index:
                left += 1
            while left < right and right == index:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

      
# 关答
class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        left, right = self.twoPointer(s, 0, len(s) - 1)            
        if left >= right:
            return True
            
        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

    def isPalindrome(self, s, left, right):
        left, right = self.twoPointer(s, left, right)
        return left >= right
        
    def twoPointer(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right

       
#Method: 自己写的第二遍 更好的办法
class Solution:
    def valid_palindrome(self, s: str) -> bool:

        valid, left, right = self.is_palindromne(s, 0, len(s) - 1)
        valid_moveleft, _, _ = self.is_palindromne(s, left + 1, right)
        valid_moveright, _, _ = self.is_palindromne(s, left, right - 1)
        return valid or valid_moveleft or valid_moveright

    def is_palindromne(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1 
            else: 
                return False, left, right
        return True, left, right
