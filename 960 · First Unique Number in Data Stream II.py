# Description
# We need to implement a data structure named DataStream. There are two methods required to be implemented:

# void add(number) // add a new number
# int firstUnique() // return first unique number
# You can assume that there must be at least one unique number in the stream when calling the firstUnique.

# Example
# Example 1:

# Input:
# add(1)
# add(2)
# firstUnique()
# add(1)
# firstUnique()
# Output:
# [1,2]
# Example 2:

#关答：单链表

class DataStream:

    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.duplicates = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.duplicates:
            return
        
        if num not in self.num_to_prev:
            self.push_back(num)            
            return
        
        # find duplicate, remove it from hash & linked list
        self.duplicates.add(num)
        self.remove(num)
    
    def remove(self, num):
        prev = self.num_to_prev.get(num)
        del self.num_to_prev[num]
        prev.next = prev.next.next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            # if we removed the tail node, prev will be the new tail
            self.tail = prev

    def push_back(self, num):
        # new num add to the tail
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        if not self.dummy.next:
            return None
        return self.dummy.next.val
    
    
#关答：双链表 O(1), O(1)
class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DataStream:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.hash = {}
    """
    @param num: next number in stream
    @return: nothing
    """
    def remove(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.tail:
            self.tail = self.tail.prev
        node.prev, node.next = None, None
        self.hash[node.value] = 0
    
    def add(self, num):
        if num in self.hash:
            if self.hash[num] == 0:
                return
            self.remove(self.hash[num])
        else:
            self.tail.next = Node(num,self.tail, None)
            self.tail = self.tail.next
            self.hash[num] = self.tail
    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        if not self.head.next:
            return -1
        return self.head.next.value
      
      
#order dict O(1), O(N)     
from collections import OrderedDict

class DataStream:

    def __init__(self):
        # do intialization if necessary
        self._mapping = OrderedDict()
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num in self._mapping:
            self._mapping[num] += 1
        else:
            self._mapping[num] = 1
    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        for key, val in self._mapping.items():
            if val == 1:
                return key
