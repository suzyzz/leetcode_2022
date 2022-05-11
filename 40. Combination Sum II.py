90 · k Sum II Algorithms
Description
Given n distinct positive integers, the integer k (1<=k<=n1<=k<=n) and a target number.
Find k distinct numbers within these n numbers such that the sum of these k numbers equals the target number, and you need to find all the solutions that satisfy the requirement (the order of the solutions is not required).

Example 1:
Input:
array = [1,2,3,4]
k = 2
target = 5
Output:
[[1,4],[2,3]]
Explanation:
1+4=5,2+3=5

Example 2:
Input:
array = [1,3,4,6]
k = 3
target = 8
Output:

[[1,3,4]]


class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        A = sorted(A)
        subsets = []
        self.dfs(A, 0, k, target, [], subsets)
        return subsets
        
    def dfs(self, A, index, k, target, subset, subsets):
        if k == 0 and target == 0:
            subsets.append(list(subset))
            return
        
        if k == 0 or target <= 0:
            return
        
        for i in range(index, len(A)):
            subset.append(A[i])
            self.dfs(A, i + 1, k - 1, target - A[i], subset, subsets)
            subset.pop()
