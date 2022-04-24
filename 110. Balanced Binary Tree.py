# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 
# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

#Method: DFS DivieConquer
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:

    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root):
        is_balanced, _ = self.DivieConquer(root)
        return is_balanced
        
    def DivieConquer(self, root):
        if not root:
            return True, 0
        
        is_left_balanced, left_height = self.DivieConquer(root.left)
        is_right_balanced, right_height = self.DivieConquer(root.right)
        
        root_height = max(left_height, right_height) + 1
        
        if not is_left_balanced or not is_right_balanced:
            return False, root_height
            
        if abs(left_height - right_height) > 1:
            return False, root_height
            
        return True, root_height
