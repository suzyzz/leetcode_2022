# Description
# Find connected component in undirected graph.
# Each node in the graph contains a label and a list of its neighbors.
# (A connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)
# You need return a list of label set.
# Nodes in a connected component should sort by label in ascending order. Different connected components can be in any order.
# Learn more about representation of graphs

# Example
# Example 1:

# Input: {1,2,4#2,1,4#3,5#4,1,2#5,3}
# Output: [[1,2,4],[3,5]]
# Explanation:

#   1------2  3
#    \     |  | 
#     \    |  |
#      \   |  |
#       \  |  |
#         4   5
# Example 2:

# Input: {1,2#2,1}
# Output: [[1,2]]
# Explanation:

#   1--2

# DFS
class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
         
    def connectedSet(self, nodes):
        self.v = {}
        for node in nodes:
            self.v[node.label] = False

        ret = []
        for node in nodes:
            if not self.v[node.label]:
                tmp = []
                self.dfs(node, tmp)
                ret.append(sorted(tmp))
        return ret

    def dfs(self, x, tmp):
        self.v[x.label] = True
        tmp.append(x.label)
        for node in x.neighbors:
            if not self.v[node.label]:
                self.dfs(node, tmp)      
             
#  BFS 遍历每个node 找联通块
from collections import deque
class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """        
    def connectedSet(self, nodes):
        result = []
        visited = set()
        
        for node in nodes:
            if node not in visited:
                subgraph = []
                self.bfs(node, visited, subgraph)
                result.append(sorted(subgraph))
        return result

    def bfs(self, node, visited, subgraph):
        queue = deque()
        queue.append(node)
        visited.add(node)
        
        while queue:
            node = queue.popleft()
            subgraph.append(node.label)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                  
#  Union Find 
class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def __init__(self):
        self.d = {}
        
    def connectedSet(self, nodes):
        # write your code here
        for n in nodes:
            self.d[n.label] = None
        for node in nodes:
            for n in node.neighbors:
                a = self.find_parent(node.label)
                b = self.find_parent(n.label)
                if a != b:
                    self.d[a] = b
        result = {}
        for k in self.d:
            key = self.find_parent(k)
            result[key] = result.get(key, []) + [k]
        # Not sure why the result must be sorted to pass... Maybe set?
        return sorted([sorted(i) for i in result.values()])
        
        
    def find_parent(self, n):
        if self.d[n] is not None:
            return self.find_parent(self.d[n])
        return n
         
