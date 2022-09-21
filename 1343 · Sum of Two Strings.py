# Description
# Given you two strings which are only contain digit character. You need to return a string spliced by the sum of the bits.

# A and B are strings which are composed of numbers
# Example
# Example1:
# Input:
# A = "99"
# B = "111"
# Output: "11010"
# Explanation: because 9 + 1 = 10, 9 + 1 = 10, 0 + 1 = 1,connect them，so answer is "11010"
# Example2:
# Input:
# A = "2"
# B = "321"
# Output: "323"
# Explanation: because 2 + 1 = 3, 2 + 0 = 2, 3 + 0 = 3, connect them，so answer is "323"


# 同向双指针-O(n)	一遍写出关答

class Solution:
    """
    @param a: a string
    @param b: a string
    @return: return the sum of two strings
    """
    def sumof_two_strings(self, a: str, b: str) -> str:
        a_index, b_index, sum_list = len(a) - 1, len(b) - 1, []
        while a_index >= 0 and b_index >= 0:
            print()
            sum_list.append(str(int(a[a_index]) + int(b[b_index]))) 
            a_index -= 1
            b_index -= 1
        while a_index >= 0 :
            sum_list.append(str(int(a[a_index]))) 
            a_index -= 1
        while b_index >= 0 :
            sum_list.append(str(int(b[b_index]))) 
            b_index -= 1

        ans = ''
        for i in range(len(sum_list) - 1, -1, -1):
            ans += sum_list[i]
        return ans

 
