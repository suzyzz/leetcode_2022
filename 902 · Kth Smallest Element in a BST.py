# Description
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example
# Example 1:

# Input：{1,#,2},2
# Output：2
# Explanation：
# 	1
# 	 \
# 	  2
# The second smallest element is 2.
# Example 2:

# Input：{2,1,3},1
# Output：1
# Explanation：
#   2
#  / \
# 1   3
# The first smallest element is 1.
# Challenge
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

#method 1:自己写的中序遍历 

class Solution:
    def kth_smallest(self, root: TreeNode, k: int) -> int:     
        answer = []
        self.in_order(root, answer)
        return answer[k - 1].val

    def in_order(self, root, answer):
        if not root:
            return 
        self.in_order(root.left, answer)
        answer.append(root)
        self.in_order(root.right, answer)
        
#method 2: 关答非递归
class Solution:
    def kthSmallest(self, root, k):
        #使用stack进行非递归算哒的数据存储
        stack = []

        #一路向左，把书的左边缘的点全部入栈
        while (root):
            stack.append(root)
            root = root.left

        # 0 到k-2总共包括k-1次操作
        # 经历k-1次才做，可以把第k个数调整到栈顶
        for i in range(k - 1):
            #前一个元素出栈
            node = stack.pop()
            # 如果出栈元素有右子树，把右子树的左边缘的点全部入栈
            if node.right:
                node = node.right
                # 一路向左，把书的左边缘的点全部入栈
                while node:
                    stack.append(node)
                    node = node.left
        #当前栈顶就是第k个元素
        return stack[-1].val

        
