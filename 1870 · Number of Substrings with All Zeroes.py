# Description
# Given a string str containing only 0 or 1, please return the number of substrings that consist of 0 .

# 1<=|str|<=30000

# Example
# Example 1:

# Input:
# "00010011"
# Output:
# 9
# Explanation:
# There are 5 substrings of "0",
# There are 3 substrings of "00",
# There is 1 substring of "000".
# So return 9
# Example 2:

# Input:
# "010010"
# Output:
# 5

# 关答-同向双指针-O(n)

class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def string_count(self, str: str) -> int:
        count, answer = 0, 0
        for i in str:
            if i == "0":
                count += 1
            else:
                answer += (count + 1) * count // 2
                count = 0
        if count != 0:
            answer += (count + 1) * count // 2
        return answer

#    自己写的同向 也不错啊
    def string_count(self, str: str) -> int:
        i, ans = 0, 0
        while i < len(str):
            while i < len(str) and str[i] == '1': 
                i += 1
            j = i
            while j < len(str) and str[j] == '0':
                j += 1
            ans += (j - i) * (j - i + 1) // 2
            i = j
        return ans
