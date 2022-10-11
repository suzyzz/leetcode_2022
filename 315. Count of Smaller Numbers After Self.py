# Description
# Give you an integer array (index from 0 to n-1, where n is the size of this array, data value from 0 to 10000) . For each element Ai in the array, count the number of elements which before Ai and smaller than it and return count number array.

# Before you do this, we suggest you complete the following three questions: Segment Tree Build， Segment Tree Query II，and Count Of Smaller Number 。

# Example
# Example 1:

# Input:
# [1,2,7,8,5]
# Output:
# [0,1,2,3,2]
# Example 2:

# Input:
# [7,8,2,1,3]
# Output:
# [0,1,0,0,2]


# 分块检索- O(n*sqrt(size))

class Block:
    def __init__(self):
        self.total = 0
        self.counter = {}
        
        
class BlockArray:
    def __init__(self, max_value):
        self.blocks = [
            Block()
            for _ in range(max_value // 100 + 1)
        ]
    
    def count_smaller(self, value):
        count = 0
        block_index = value // 100
        for i in range(block_index):
            count += self.blocks[i].total
        
        counter = self.blocks[block_index].counter
        for val in counter:
            if val < value:
                count += counter[val]
        return count
        
    def insert(self, value):
        block_index = value // 100
        block = self.blocks[block_index]
        block.total += 1
        block.counter[value] = block.counter.get(value, 0) + 1


class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def count_of_smaller_number_i_i(self, A):
        if not A:
            return []

        block_array = BlockArray(10000)
        results = []
        for a in A:
            count = block_array.count_smaller(a)
            results.append(count)
            block_array.insert(a)
        return results
      
      
   class BITree:
    def __init__(self, num_range):
        self.bit = [0] * (num_range + 1)
    
    def get_prefix_sum(self, index):
        result = 0
        index = index + 1
        while index > 0:
            result += self.bit[index]
            index -= self._lowbit(index)
        
        return result
    
    def increase_count(self, index, delta):
        index = index + 1
        while index < len(self.bit):
            self.bit[index] += delta
            index += self._lowbit(index)
    
    def _lowbit(self, x):
        return x & (-x)
      
      
      
# BIT - Binary Indexed Tree
class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def count_of_smaller_number_i_i(self, A):
        bitree = BITree(10000)
        results = []
        
        for num in A:
            smaller_count = bitree.get_prefix_sum(num - 1)
            results.append(smaller_count)
            bitree.increase_count(num, 1)
        
        return results
