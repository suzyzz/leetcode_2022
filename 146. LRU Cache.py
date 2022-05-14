# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 
  
  #Method 1:单链表
class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):	#将数据移动至尾部
        node = prev.next
        if node == self.tail:
            return
        
        # remove the current node from linked list
        prev.next = node.next
        # update the previous node in hash map
        self.key_to_prev[node.next.key] = prev
        node.next = None

        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        
        prev = self.key_to_prev[key]
        current = prev.next
        
        self.kick(prev)
        return current.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.key_to_prev:	   
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return
        
        self.push_back(LinkedNode(key, value))  #如果key不存在，则存入新节点
        if len(self.key_to_prev) > self.capacity:		#如果缓存超出上限
            self.pop_front()					#删除头部
            
   #双链表
  class Node:
    def __init__(self, key= None, value = None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
        
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}
        self.head = Node(-1,-1) # dummy node
        self.tail = Node(-1, -1) # dummy node
        self.tail.prev = self.head
        self.head.next = self.tail
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.hash: return -1 
        node = self.hash[key]
        self.remove_node(node)
        self.move_to_tail(node)
        return node.val 
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if self.get(key) != -1:
            self.hash[key].val = value
            return 
        if len(self.hash) >= self.capacity:
            self.pop_front()
        node = Node(key, value)
        self.move_to_tail(node)
        self.hash[key] = node
        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def move_to_tail(self, node):
        node.prev = self.tail.prev 
        node.next = self.tail 
        node.prev.next = node 
        self.tail.prev = node
        
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

#OrderedDict
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        ## pop value and insert to the bottom of queue
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last = False)
        self.cache[key] = value
