# Description
# Six degrees of separation is a philosophical problem, which means that everyone and everything can be connected through six steps or less.
# Now give you a friendship, calculate how many steps two people can be connected through, if not, return -1.

# Example
# Example1

# Input: {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4 
# Output: 2
# Explanation:
#     1------2-----4
#      \          /
#       \        /
#        \--3--/
# Example2

# Input: {1#2,4#3,4#4,2,3} and s = 1, t = 4
# Output: -1
# Explanation:
#     1      2-----4
#                  /
#                /
#               3

# 单队列 -  通用模板	一遍写出关答

"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

import collections
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        if not s or not t or not graph:
            return -1
        queue = collections.deque([s])
        visited = {s}
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in node.neighbors:
                    if neighbor == t:
                        return step
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            
        return -1
                
            
