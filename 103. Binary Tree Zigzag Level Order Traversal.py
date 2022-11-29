# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
  
# Example 2:
# Input: root = [1]
# Output: [[1]]
  
# Example 3:
# Input: root = []
# Output: []

# BFS - 一边写出关答
import collections
class Solution:
    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        level = 1
        queue = collections.deque([root])
        while queue:
            level += 1
            current_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    current_level.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    current_level.append(node.right.val)
                    queue.append(node.right)
            if level % 2 == 0:
                current_level.reverse()
            ans.append(current_level)
        return ans[:-1]

