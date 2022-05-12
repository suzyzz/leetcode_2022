# Description
# In data structure Hash, hash function is used to convert a string(or any other type) into an integer smaller than hash size and bigger or equal to zero. The objective of designing a hash function is to "hash" the key as unreasonable as possible. A good hash function can avoid collision as less as possible. A widely used hash function algorithm is using a magic number 33, consider any string as a 33 based big integer like follow:
# hashcode("abcd")hashcode("abcd")
# =(ascii(a) * 33^3+ascii(b) * 33^2+ascii(c) * 33 +ascii(d))=(ascii(a)∗33 
# 3
#  +ascii(b)∗33 
# 2
#  +ascii(c)∗33+ascii(d)) % HASH_SIZE
# = (97* 33^3+ 98*33^2+ 99* 33 +100)=(97∗33 
# 3
#  +98∗33 
# 2
#  +99∗33+100) % HASH_SIZE
# = 3595978=3595978 % HASH_SIZE
# here HASH_SIZE is the capacity of the hash table (you can assume a hash table is like an array with index 00 ~ HASH_SIZE-1).Given a string as a key and the size of hash table, return the hash value of this key.

# For this problem, you are not necessary to design your own hash algorithm or consider any collision issue, you just need to implement the algorithm as described.
# 0 <= len(key) <= 1000000<=len(key)<=100000

# Example
# Example 1:

# Input:  key="abcd", size = 1000
# Output: 978
# Explanation: (97*33^3 + 98*33^2 + 99*33 + 100*1)%1000 = 978
# Example 2:

# Input:  key="abcd", size = 100
# Output: 78
# Explanation: (97*33^3 + 98*33^2 + 99*33 + 100*1)%100 = 78


class Solution:
    def hashCode(self, key, HASH_SIZE):
        ans = 0
        for x in key:
            ans = (ans * 33 + ord(x)) % HASH_SIZE
        return ans
