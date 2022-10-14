# Description
# Return the number of nodes in the kth layer(The layer number starts from 1 and the root node is layer 1).

# Example
# Example1
# Input: root = {3,9,20,#,#,15,7}, k = 2
# Output: 2
# Explanation:
#   3
#  / \
# 9  20
#   /  \
#  15   7
               
# Example2
# Input: root = {3,1,2}, k = 1
# Output: 1
# Explanation:
#   3
#  / \
# 1   2

# 单队列 -  通用模板	一遍写出关答
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
import collections
class Solution:
    """
    @param root: the root node
    @param k: an integer
    @return: the number of nodes in the k-th layer of the binary tree
    """
    def kthfloor_node(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        queue = collections.deque([root])
        layer = 0
        while queue:
            layer += 1
            n = len(queue)
            if layer == k:
                return n
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return 0
