# Description
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# Given binary search tree: root = {6,2,8,0,4,7,9,#,#,3,5}
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
# Example
# Example 1:

# Input: 
# {6,2,8,0,4,7,9,#,#,3,5}
# 2
# 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# 一遍关答 - DC

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return
        if (p.val <= root.val and q.val >= root.val) or (q.val <= root.val and p.val >= root.val):
            return root
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
