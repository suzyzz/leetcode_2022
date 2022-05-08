# Description
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example
# Example1

# Input: root = {5,4,9,2,#,8,10} and target = 6.124780
# Output: 5
# Explanation：
# Binary tree {5,4,9,2,#,8,10},  denote the following structure:
#         5
#        / \
#      4    9
#     /    / \
#    2    8  10
# Example2

# Input: root = {3,2,4,1} and target = 4.142857
# Output: 4
# Explanation：
# Binary tree {3,2,4,1},  denote the following structure:
#      3
#     / \
#   2    4
#  /
# 1

#关答：非递归
class Solution:
    def closestValue(self, root, target):
        upper = root
        lower = root
        while root:
            if target > root.val:
                lower = root
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val
        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val
        return lower.val
      
 #关答： 递归
class Solution:
    def closestValue(self, root, target):
        if root is None:
            return None
            
        lower = self.get_lower_bound(root, target)
        upper = self.get_upper_bound(root, target)
        if lower is None:
            return upper.val
        if upper is None:
            return lower.val
            
        if target - lower.val < upper.val - target:
            return lower.val
        return upper.val
        
    def get_lower_bound(self, root, target):
        # get the largest node that < target
        if root is None:
            return None
        
        if target < root.val:
            return self.get_lower_bound(root.left, target)

        # root.val <= target, root已经是一个lower bound
        #继续在右子树寻找更接近target的lower bound    
        lower = self.get_lower_bound(root.right, target)
        # 如果找到了更接近target的lower bound 返回，否则返回root
        return root if lower is None else lower
        
    def get_upper_bound(self, root, target):
        # get the smallest node that >= target
        if root is None:
            return None
        
        if target >= root.val:
            return self.get_upper_bound(root.right, target)
            
        # root.val > target, root已经是一个upper bound
        #继续在左子树寻找更接近target的upper bound   
        upper = self.get_upper_bound(root.left, target)
        # 如果找到了更接近target的upper bound 返回，否则返回root
        return root if upper is None else upper
