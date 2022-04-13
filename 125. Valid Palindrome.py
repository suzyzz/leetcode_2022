# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# Method 1: Two pointer (关答）
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
      
 # Method 2: 枚举法
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s):
        # write your code here
        result=''
        for i in s:
            if i.isalnum():
                result+=i.lower()
        if result==result[::-1]:
            return True
        return False
      
 #自己写的枚举     
 class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s):
        # write your code here
        string = ''.join(e for e in s.lower() if e.isalnum())
        out=True
        for i in range(int((len(string) & -2)/2)):
                if string[i] != string[-i-1]:
                    out=False
        return out
      
 #自己写的two pointer       
 class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s):

        s = s.lower()
        start, end = 0, len(s) - 1 
        while start < end:
            if not s[start].isalnum():
                start += 1 
                continue
            if not s[end].isalnum():
                end -= 1 
                continue 
            if s[start] != s[end]:
                return False  
            start += 1 
            end -= 1 
        return True
