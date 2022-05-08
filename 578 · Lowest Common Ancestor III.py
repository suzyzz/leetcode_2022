# Description
# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
# The nearest common ancestor of two nodes refers to the nearest common node among all the parent nodes of two nodes (including the two nodes).
# Return null if LCA does not exist.

# node A or node B may not exist in tree.
# Each node has a different value

# Example
# Example1

# Input: 
# {4, 3, 7, #, #, 5, 6}
# 3 5
# 5 6
# 6 7 
# 5 8
# Output: 
# 4
# 7
# 7
# null
# Explanation:
#   4
#  / \
# 3   7
#    / \
#   5   6

# LCA(3, 5) = 4
# LCA(5, 6) = 7
# LCA(6, 7) = 7
# LCA(5, 8) = null
# Example2

# Input:
# {1}
# 1 1
# Output: 
# 1
# Explanation:
# The tree is just a node, whose value is 1.



#关答
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
import copy
class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """ 
    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.helper(root, A, B)
        #如果AB都存在才返回
        return lca if a and b else None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None
            
        #分别墙应左右子树寻找A，B
        left_a, left_b, left_node = self.helper(root.left, A, B)
        right_a, right_b, right_node = self.helper(root.right, A, B)
        
        #如果左边有A，或者右边有A，或者root本身是A，那么root这棵树有A
        a = left_a or right_a or root == A
        #如果左边有B，或者右边有B，或者root本身是B，那么root这棵树有B
        b = left_b or right_b or root == B
        
        #如果root为A或者B，返回root（当前root有可能为LCA）
        if root == A or root == B:
            return a, b, root

        # 如果A，B分别存在于两颗子树，root为LCA，返回root
        if left_node is not None and right_node is not None:
            return a, b, root
        # 左子树有一个点或者左子树有LCA
        if left_node is not None:
            return a, b, left_node
        # 右子树有一个点或者右子树有LCA
        if right_node is not None:
            return a, b, right_node
        #左右啥都没有
        return a, b, None




