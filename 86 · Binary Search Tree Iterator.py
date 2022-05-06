# Description
# Design an iterator over a binary search tree with the following rules:
# Next() returns the next smallest element in the BST.

# Elements are visited in ascending order (i.e. an in-order traversal)
# next() and hasNext() queries run in O(1)O(1) time in average.
# Example
# Example 1:

# Input:tree = {10,1,11,#,6,#,12}
# Output:[1,6,10,11,12]
# Explanation:
# The BST is look like this:
# 10
# / \
# 1     11
# \      \
# 6       12
# You can return the inorder traversal of a BST [1, 6, 10, 11, 12]

# Example 2:

# Input:tree = {2,1,3}
# Output:[1,2,3]
# Explanation:
# The BST is look like this:
# 2
# /  \
# 1     3
# You can return the inorder traversal of a BST [1,2,3]

#关答-精华版 非递归DFS 阅读全文并背诵
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.find_most_left(root)

    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        return bool(self.stack)

    def _next(self):
        node = self.stack.pop()
        if node.right:
            self.find_most_left(node.right)
        return node
      
#关答 非递归DFS 阅读全文并背诵
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def _next(self):
        node = self.stack[-1]
        if node.right is not None:
            n = node.right
            while n != None:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        
        return node





