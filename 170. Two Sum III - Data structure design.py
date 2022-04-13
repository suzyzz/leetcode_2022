# Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

# Implement the TwoSum class:

# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
 

# Example 1:

# Input
# ["TwoSum", "add", "add", "add", "find", "find"]
# [[], [1], [3], [5], [4], [7]]
# Output
# [null, null, null, null, true, false]

# Explanation
# TwoSum twoSum = new TwoSum();
# twoSum.add(1);   // [] --> [1]
# twoSum.add(3);   // [1] --> [1,3]
# twoSum.add(5);   // [1,3] --> [1,3,5]
# twoSum.find(4);  // 1 + 3 = 4, return true
# twoSum.find(7);  // No two integers sum up to 7, return false
 

# Constraints:

# -105 <= number <= 105
# -231 <= value <= 231 - 1
# At most 104 calls will be made to add and find.


# Method 1, 自己写的 (Fail) Brute Force + Two Pointer (Over time) 
class TwoSum:
    def __init__(self):
        self.data = []
    
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        # if number not in self.data:
        self.data.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        # if not self.data or not value:
        #     return False

        for i in range(len(self.data)):
            for j in range(1, len(self.data) - i):
                if self.data[i] + self.data[i + j] == value:
                    return True

        return False
  
  
  
#   Method 2: 排序数组+双指针的算法会超时
  class TwoSum:
    
    def __init__(self):
        self.nums = []
        
    def add(self, number):
        self.nums.append(number)
        index = len(self.nums) - 1
        while index > 0 and self.nums[index - 1] > self.nums[index]:
            temp = self.nums[index - 1]
            self.nums[index - 1] = self.nums[index]
            self.nums[index] = temp
            index -= 1

    def find(self, value):
        left, right = 0, len(self.nums) - 1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < value:
                left += 1
            elif two_sum > value:
                right -= 1
            else:
                return True
        return False
      
#    Method 3: Hash Table
class TwoSum(object):

    def __init__(self):
        self.count = {}
        
    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    def find(self, value):
        for num in self.count:
            if value - num in self.count and \
                (value - num != num or self.count[num] > 1):
                return True
        return False
