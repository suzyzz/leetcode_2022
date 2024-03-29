# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

#Method1: 单队列BFS
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
    def levelOrder(self, root):
        if root is None:
            return []
        # step1: 把第一层的节点放到队列当中
        queue = collections.deque([root])
        results = []
        # step2： while队列非空
        while queue:
            results.append([node.val for node in queue])
            # step3：把上一层节点，拓展出下一层节点
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return results
       
       
#Method2: 双队列BFS
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        queue = [root]
        results = []
        
        while queue:
            next_queue = []
            results.append([node.val for node in queue])
            
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return results
  
  
#Method: Dummy Node
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        queue = collections.deque([root, None])
        results, level = [], []
        
        while queue:
            node = queue.popleft()
            if node is None:
                results.append(level)
                if queue:
                    queue.append(None)
                    continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results

       
       
       
       
       
#     双队列 - deque versiono 自己写对
    def level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        next_level = collections.deque()
        result = []
        level = []
        while queue:
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not queue:
                result.append(level)
                level = []
                queue = next_level
                next_level = collections.deque()
        
        return result
                
