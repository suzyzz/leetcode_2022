# 递归遍历
  def inorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)

# 非递归遍历
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        answer = []
        stack = [root]
        curr = root
        while curr.left:
            stack.append(curr.left)
            curr = curr.left

        while stack:
            curr = stack.pop()
            answer.append(curr.val)
            if curr.right:
                stack.append(curr.right)
                new = curr.right
                while new.left:
                    stack.append(new.left)
                    new = new.left
        return answer
