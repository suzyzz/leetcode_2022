# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

#Method: DFS - traversal - reccursion 关答
class Solution:
    def binary_tree_paths(self, root):
        if not root:
            return []
        
        paths = []
        self.find_paths(root, [root], paths)
        return paths
    
    def find_paths(self, node, path, paths):
        if not node:
            return
        
        if not node.left and not node.right:
            paths.append('->'.join([str(n.val) for n in path]))
            return
            
        path.append(node.left)
        self.find_paths(node.left, path, paths)
        path.pop()
        
        path.append(node.right)
        self.find_paths(node.right, path, paths)
        path.pop()

        
#Method: Divide and Conquer        
class Solution:
    def binary_tree_paths(self, root):
        paths = []
        if not root:
            return paths
        if not root.left and not root.right:
            return [str(root.val)]
        
        for path in self.binary_tree_paths(root.left):
            paths.append(str(root.val) + "->" + path)
        for path in self.binary_tree_paths(root.right):
            paths.append(str(root.val) + "->" + path)
        
        return paths

# 自己写的traversal 没官答简洁 但时间一样
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        self.traversal(root, paths, [])
        return paths
    
    def traversal(self, root, paths, path):
        path.append(root)
        if not root.left and not root.right:
            paths.append('->'.join([str(node.val) for node in path]))
        if root.left:
            self.traversal(root.left, paths, path)
            path.pop()
        if root.right:
            self.traversal(root.right, paths, path)
            path.pop()
       
 
