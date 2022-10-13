# Description
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Example
# Example 1:

# Input: {}
# Output: 0
# Example 2:

# Input:  {1,#,2,3}
# Output: 3	
# Explanation:
# 	1
# 	 \ 
# 	  2
# 	 /
# 	3    
# it will be serialized {1,#,2,3}
# Example 3:

# Input:  {1,2,3,#,#,4,5}
# Output: 2	
# Explanation: 
#       1
#      / \ 
#     2   3
#        / \
#       4   5  
# it will be serialized {1,2,3,#,#,4,5}


# BFS - 自己写出关答
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
    @param root: The root of binary tree
    @return: An integer
    """
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
      
      
# DC DFS
    def minDepth(self, root):
        if root is None:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        # 当左子树或右子树为空时，最小深度取决于另一颗子树
        if leftDepth == 0 or rightDepth == 0:
            return leftDepth + rightDepth + 1
        return min(leftDepth, rightDepth) + 1

