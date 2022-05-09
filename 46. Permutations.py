# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 
# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

#关答：DFS
class Solution:
    def permute(self, nums):
        if not nums:
            # 0! = 1
            return [[]]
            
        permutations = []
        self.dfs(nums, [], set(), permutations)
        return permutations
        
    # 递归的定义：找到所有permutation开头的permutations
    def dfs(self, nums, permutation, visited, permutations):
        # 递归的出口，如果所有element都收到了就深度复制
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return
        
        # 递归的拆解
        # [] -> [1], [2], [3]
        # [1] -> [1,2], [1,3]..
        for num in nums:
            if num in visited:
                continue
            permutation.append(num)
            visited.add(num)
            self.dfs(nums, permutation, visited, permutations)
            visited.remove(num)
            permutation.pop()
#其实不需要visited也可以， 因为visited == permutations, list也可以用来判断 if in list
class Solution:
    def permute(self, nums):
        if not nums:
            return [[]]
            
        permutations = []
        self.dfs(nums, [], permutations)
        return permutations

    def dfs(self, nums, permutation, permutations):
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return

        for num in nums:
            if num in permutation:
                continue
            permutation.append(num)
            self.dfs(nums, permutation, permutations)
            permutation.pop()
