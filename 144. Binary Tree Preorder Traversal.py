# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:
# Input: root = []
# Output: []
# Example 3:
# Input: root = [1]
# Output: [1]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# 自己写的递归遍历  
class Solution:
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        answer = []
        self.trave(root, answer)
        return answer

    def trave(self, root, answer):
        if not root:
            return
        answer.append(root.val)
        if root.left:
            self.trave(root.left, answer)
        if root.right:
            self.trave(root.right, answer)
            
# 自己写的非递归遍历    跟关答一样        
     def preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        answer = []
        stack = [root]
        while stack:
            curr = stack.pop()
            answer.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return answer
      
      
# 关答Version 1: Recursion   
class Solution:
    def preorderTraversal(self, root):
        self.results = []
        self.traverse(root)
        return self.results
        
    def traverse(self, root):
        if root is None:
            return
        self.results.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

# 关答Version 2: Non-Recursion  
class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder
      
# 巧妙递归
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorder_traversal(root.left) + self.preorder_traversal(root.right)
