# Description
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Assume the length of given string will not exceed 100000.

# Example
# Example 1:

# Input : s = "abccccdd"
# Output : 7
# Explanation :
# One longest palindrome that can be built is "dccaccd", whose length is `7`.

# Method 1: Hash function
class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    
    # the answer is the count of characters that has even number of appereances.
    # for characters that has odd number of appereances,
    # their appereances minus 1 will make their apperances even.
    # And finally we can put an unused character in the middle of the palindrome
    def longestPalindrome(self, s):
        # Write your code here
        hash = {}

        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True

        remove = len(hash) #落单的char，如果有落单的放一个在中间
        if remove > 0:
            remove -= 1
    
        return len(s) - remove

# Method 2:贪心    
class Solution:
    def longestPalindrome(self, s):       
             
        ans = 0 #ans为最终答案
        cnt = collections.Counter(s) #cnt统计字符串s中每种字母出现次数的计数数组

        for i in cnt.values():
            ans += i // 2 * 2 #每种字符可使用cnt/2*2次
            if ans % 2 == 0 and i % 2 == 1:
                ans += 1 #如果遇到出现奇数次的字符并且中心位置空着，那么答案加1
                
        return ans   
      
      
      
# Method 3: 花花
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s):
        # write your code here
        freqs = [0] * 128
        
        for c in s:
            freqs[ord(c)] += 1
        
        ans, odd = 0, 0
        for freq in freqs:
            ans += freq & (~1) #~1 => -2; 7&-2 => 6 最近偶数
            odd |= freq & 1 #7&1 => 1 偶数=0， 奇数=1； |= => 0或者1
        
        return ans + odd
        
