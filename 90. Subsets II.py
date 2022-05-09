# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 
# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

#Method 1： Backtrack关答
class Solution:
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, k, subset, res):
        res.append(subset[:])
        for i in range(k, len(nums)):
            # 剪枝
            if (i != k and nums[i] == nums[i - 1]):
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, res)
            subset.pop()

            
            
#Method 2： Hashset
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        subsets = []
        visited = {}
        nums.sort()
        self.dfs(nums, 0, [], subsets, visited)
        
        return subsets

    def get_hash(self, subset):
        hash_string = "-".join([str(num) for num in subset])
        return hash_string
        
    def dfs(self, nums, start_index, subset, subsets, visited):
        hash_string = self.get_hash(subset)
        if hash_string in visited:
            return;
        
        visited[hash_string] = True
        subsets.append(list(subset))
        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets, visited)
            subset.pop()
            
            
#Method 3： Magic
class Solution:
    def subsetsWithDup(self, S):
        S.sort()
        p = [[S[x] for x in range(len(S)) if i>>x&1] for i in range(2**len(S))]
        func = lambda x,y:x if y in x else x + [y]
        p = reduce(func, [[], ] + p)
        return list(reversed(p))
