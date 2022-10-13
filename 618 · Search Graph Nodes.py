# Description
# Given a undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.
# There is a mapping store the nodes' values in the given parameters.
# It's guaranteed there is only one available solution

# Example
# Example 1:
# Input:
# {1,2,3,4#2,1,3#3,1,2#4,1,5#5,4}
# [3,4,10,50,50]
# 1
# 50
# Output:
# 4
# Explanation:
# 2------3  5
#  \     |  | 
#   \    |  |
#    \   |  |
#     \  |  |
#       1 --4
# Give a node 1, target is 50

# there a hash named values which is [3,4,10,50,50], represent:
# Value of node 1 is 3
# Value of node 2 is 4
# Value of node 3 is 10
# Value of node 4 is 50
# Value of node 5 is 50

# Return node 4
 
# Example 2:
# Input:
# {1,2#2,1}
# [0,1]
# 1
# 1
# Output:
# 2
 
#  单队列 -  通用模板	一遍写出关答

 
 """
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import collections

class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        queue = collections.deque([node])
        visited = {node}
        while queue:
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                if values[curr_node] == target:
                    return curr_node
                for neighbor in curr_node.neighbors:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
        return 
        
        # 为什么是nearest node 不是the node？ 
        # 如果node.val = target 那个node就是结果啊 如果没有等于的就return Null了


 
 
 
 
 
 
 
 
 
 
 
 
