# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
 
# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

#DFS
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        res = []
        used = [False] * len(nums)
        path = []
        # 排序
        nums = sorted(nums)
        # dfs
        self.dfs(nums, used, path, res)
        return res
    def dfs(self, nums, used, path, res):
        # 叶子节点
        if len(path) == len(nums):
            res.append(path[:])
            return
        # 非叶节点
        for i in range(len(nums)):
            # 元素已访问过 或者 是重复元素
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            # 在路径添加该节点，递归
            used[i] = True
            self.dfs(nums, used, path + [nums[i]], res)
            # 回溯
            used[i] = False
