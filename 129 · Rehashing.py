# Description
# The size of the hash table is not determinate at the very beginning. If the total size of keys is too large (e.g. size >= capacity / 10), we should double the size of the hash table and rehash every keys. Say you have a hash table looks like below:

# size=3, capacity=4

# [null, 21, 14, null]
#        ↓    ↓
#        9   null
#        ↓
#       null
# The hash function is:

# int hashcode(int key, int capacity) {
#     return key % capacity;
# }
# here we have three numbers, 9, 14 and 21, where 21 and 9 share the same position as they all have the same hashcode 1 (21 % 4 = 9 % 4 = 1). We store them in the hash table by linked list.

# rehashing this hash table, double the capacity, you will get:

# size=3, capacity=8

# index:   0    1    2    3     4    5    6   7
# hash : [null, 9, null, null, null, 21, 14, null]
# Given the original hash table, return the new hash table after rehashing .

# For negative integer in hash table, the position can be calculated as follow:

# C++/Java: if you directly calculate -4 % 3 you will get -1. You can use function: a % b = (a % b + b) % b to make it is a non negative integer.
# Python: you can directly use -1 % 3, you will get 2 automatically.
# 0 <= capacity <= 20000<=capacity<=2000
# 0 <= size <= 100000<=size<=10000

# Example
# Example 1:

# Input:

# hashTable = [null, 21->9->null, 14->null, null]
# Output:

# [null, 9->null, null, null, null, 21->null, 14->null, null]

#关答
class Solution:
    def rehashing(self,hashTable):
        HASH_SIZE = 2 * len(hashTable)
        anshashTable = [None for i in range(HASH_SIZE)]
        for item in hashTable:
            p = item
            while p != None:
                self.addnode(anshashTable,p.val)
                p = p.next
        return anshashTable

    def addnode(self, anshashTable, number):
        p = number % len(anshashTable)
        if anshashTable[p] == None: #如果在新的table里还没有这个数，加上一个新ListNode
            anshashTable[p] = ListNode(number)
        else:
            self.addlistnode(anshashTable[p], number) #如果在新的table有这个数，加在next里

    def addlistnode(self, node, number):
        if node.next != None:
            self.addlistnode(node.next, number) #如果新的node有next，加在next->next-> ... next->的末尾
        else:
            node.next = ListNode(number) #如果新的node没有next，作为第一个next 连起来





