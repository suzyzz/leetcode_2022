# Description
# Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
# The range of input and output data is in int.

# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

# Example
# Example 1:

# Input:
# {1,-5,2,1,2,-4,-5}
# Output:1
# Explanation:
# The tree is look like this:
#      1
#    /   \
#  -5     2
#  / \   /  \
# 1   2 -4  -5 
# The sum of whole tree is minimum, so return the root.
# Example 2:

# Input:
# {1}
# Output:1
# Explanation:
# The tree is look like this:
#    1
# There is one and only one subtree in th

#关答， 有全局变量
class Solution:
    def find_subtree(self, root: TreeNode) -> TreeNode:
        self.min_sum = float('inf')
        self.min_sum_root = None

        self.divide_conqure(root)
        return self.min_sum_root

    def divide_conqure(self, root):
        if root is None:
            return 0
        left_sum = self.divide_conqure(root.left)
        right_sum = self.divide_conqure(root.right)
        tree_sum = left_sum + right_sum + root.val
        if tree_sum < self.min_sum:
            self.min_sum = tree_sum
            self.min_sum_root = root
        return tree_sum
      
#关答， 没全局变量
class Solution:
    def find_subtree(self, root: TreeNode) -> TreeNode:
        mininum, subtree, sum_of_root = self.divide_conqure(root)
        return subtree

    def divide_conqure(self, root):
        if root is None:
            return sys.maxsize, None, 0
        left_mininum, left_subtree, left_sum = self.divide_conqure(root.left)
        right_mininum, right_subtree, right_sum = self.divide_conqure(root.right)

        sum_of_root = left_sum + right_sum + root.val
        if left_mininum == min(left_mininum, right_mininum, sum_of_root):
            return left_mininum, left_subtree, sum_of_root
        if right_mininum == min(left_mininum, right_mininum, sum_of_root):
            return right_mininum, right_subtree, sum_of_root
        return sum_of_root, root, sum_of_root
