# Description
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# Example
# Example 1:
# Input:
# tree = {1,2,3}
# Output:
# [[2,3],[1]]
# Explanation:
#     1
#    / \
#   2   3
# it will be serialized {1,2,3}

# Example 2:
# Input
# tree = {3,9,20,#,#,15,7}
# Output:
# [[15,7],[9,20],[3]]
# Explanation:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# it will be serialized {3,9,20,#,#,15,7}



# BFS - 单队列 + 反转  O（N+M)

from typing import (
    List,
)
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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        results = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level)
        results = results[::-1]
        return results
