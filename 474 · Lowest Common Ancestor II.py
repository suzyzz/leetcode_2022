# Description
# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

# The lowest common ancestor of two nodes refers to the lowest common node among all the parent nodes of two nodes (including the two nodes).

# In addition to the left and right son pointers, each node also contains a father pointer, parent, pointing to its own father.

# Example
# Example 1:

# Input：{4,3,7,#,#,5,6},3,5
# Output：4
# Explanation：
#      4
#      / \
#     3   7
#        / \
#       5   6
# LCA(3, 5) = 4
# Example 2:

# Input：{4,3,7,#,#,5,6},5,6
# Output：7
# Explanation：
#       4
#      / \
#     3   7
#        / \
#       5   6
# LCA(5, 6) = 7


#关答1 思路1： 找到A的所有路径，再遍历B第一次出现的parent
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        parent_set = set()
        # 把A的祖先节点加入到哈希表中
        curr = A
        while curr is not None:
            parent_set.add(curr)
            curr = curr.parent
        # 遍历B的祖先节点，第一个在哈希表中出现的即为答案
        curr = B
        while curr is not None:
            if curr in parent_set:
                return curr
            curr = curr.parent
        return None

# 	思路2：找到A，B的所有路径，从前往后找最后一个comment node

