# Description
# Given an directed graph, a topological order of the graph nodes is defined as follow:

# For each directed edge A -> B in graph, A must before B in the order list.
# The first node in the order can be any node in the graph with no nodes direct to it.
# Find any topological order for the given graph.

# You can assume that there is at least one topological order in the graph.
# Learn more about representation of graphs

# The number of graph nodes <= 5000
# Example
# Example 1:

# Input:

# graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}
# Output:

# [0, 1, 2, 3, 4, 5]


#关答
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        node_to_indegree = self.get_indegree(graph)

        # bfs
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
                
        return order
    
    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
                
        return node_to_indegree
      
#自己写的不过 问助教 在等答案

"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
import collections
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        graph_array = {x.label: [y.label for y in x.neighbors] for x in graph}
        in_degree = {x.label:0 for x in graph}
        print(graph_array)
        print(in_degree)

        queue = collections.deque()
        topo_order = []

        for key in in_degree.keys():
            if in_degree[key] == 0:
                queue.append(key)
        
        while queue:
            current_node = queue.popleft()
            topo_order.append(current_node)
            for next_node in graph_array[current_node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node.label)

        return topo_order
    
# 20221027 - 自己写的一次过 跟关答一样时间/方法
    def topSort(self, graph):
        in_degree, order = {}, []
        for node in graph:
            in_degree[node] = in_degree.get(node, 0)
            for neighbor in node.neighbors:
                in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
        queue = collections.deque([])
        for key, val in in_degree.items():
            if val == 0:
                queue.append(key)

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == len(graph) else []
            












