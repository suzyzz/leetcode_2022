# Description
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# The answer will not exceed 5000

# Example
# Example 1:
# Input:
# tree = {}
# Output:
# 0
# Explanation:
# The height of empty tree is 0.

# Example 2:
# Input:
# tree = {1,2,3,#,#,4,5}
# Output:
# 3
# Explanation:
# Like this:
# 1
# / \
# 2   3
# /  \
# 4    5
# it will be serialized {1,2,3,#,#,4,5}

# 关答 - DC
    def maxDepth(self, root):
        if root is None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1
      
# 自己写的 DC
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dc(root, 0)
    
    def dc(self, node, depth):
        if not node:
            return depth
        depth += 1
        left_depth = self.dc(node.left, depth)
        right_depth = self.dc(node.right, depth)
        return max(left_depth, right_depth)
