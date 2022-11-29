# 递归遍历
def postorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorder_traversal(root.left) + self.postorder_traversal(root.right) + [root.val]
# 非递归遍历

    def postorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans, stack, cur = [], [], root
        while cur:
            stack.append(cur)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right 
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            if stack and stack[-1].left == cur:
                cur = stack[-1].right
                while cur:
                    stack.append(cur)
                    if cur.left:
                        cur = cur.left
                    else:
                        cur = cur.right
        
        return ans
