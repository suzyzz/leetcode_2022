# Description
# Flatten a binary tree to a fake "linked list" in pre-order traversal.

# Here we use the right pointer in TreeNode as the next pointer in ListNode.

# Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

# Example
# Example 1:

# Input:{1,2,5,3,4,#,6}
# Output：{1,#,2,#,3,#,4,#,5,#,6}
# Explanation：
#      1
#     / \
#    2   5
#   / \   \
#  3   4   6

# 1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6
# Example 2:

# Input:{1}
# Output:{1}
# Explanation：
#          1
#          1

#mtehod 1: Divide Conquer

class Solution:
    def flatten(self, root):
        self.flatten_and_return_last_node(root)
        
    # restructure and return last node in preorder
    def flatten_and_return_last_node(self, root):
        if root is None:
            return None
            
        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)
        
        # connect 
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
            
        return right_last or left_last or root

#mtehod 2: Pre-order traversal        
class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        if not root:
            return
        
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
          
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left) 
            
            node.left = None
            
            if stack:
                node.right = stack[-1]
            else:
                node.right = None
