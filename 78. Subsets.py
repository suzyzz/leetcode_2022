# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

#Method 1: DFS Divide Conquer
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums:
            return [results]
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results
    
    # 递归的定义
    def dfs(self, nums, index, subsets, results):
        # 递归的出口
        if index == len(nums):
            results.append(list(subsets))
            return
        # 递归的拆解
        # 选 nums[index]
        subsets.append(nums[index])
        self.dfs(nums, index + 1, subsets, results)
        # 不选 nums[index]
        subsets.pop()
        self.dfs(nums, index + 1, subsets, results)
        
#Method 2: DFS Backtrack (Faster)
class Solution:
    def subsets(self, nums):
        res = []
        # 排序
        nums.sort()
        # dfs搜索
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, k, subset, res):
        # 当前组合存入res
        res.append(subset[:])
        # 为subset新增一位元素
        for i in range(k, len(nums)):
            subset.append(nums[i])
            # 下一层搜索
            self.dfs(nums, i + 1, subset, res)
            # 回溯
            subset.pop()

#         Method 4    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = [[]]
        for num in nums:
            output.extend([subset + [num] for subset in output])
        return output

 # Method 5 - BFS    
        def subsets(self, nums: List[int]) -> List[List[int]]:
        queue = [[]]
        index = 0
        while index < len(queue):
            subset = queue[index]
            index += 1
            for num in nums:
                if subset and subset[-1] >= num:
                    continue
                queue.append(subset + [num])
        return queue
    
    
  # Method 6 - BFS
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        queue = [[]]
        for num in nums:
            for i in range(len(queue)):
                subset = list(queue[i])
                subset.append(num)
                queue.append(subset)
        return queue
