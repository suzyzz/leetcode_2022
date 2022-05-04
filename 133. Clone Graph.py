# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# class Node {
#     public int val;
#     public List<Node> neighbors;
# } 

# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

#clean version
import collections
class Solution:
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        if not node:
            return None

        nodes = self.find_nodes_by_bfs(node)
        mapping = self.copy_nodes(nodes)
        self.copy_edges(mapping)
        
        return mapping[node]
    
    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node]) 
        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor in visited: 
                    continue
                queue.append(neighbor)
                visited.add(neighbor) 
        return list(visited)
        
    def copy_nodes(self, nodes):
        mapping = {}   
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping

    def copy_edges(self, mapping):
        for node in mapping.keys(): 
            new_node = mapping[node] 
            for neighbor in node.neighbors:
                new_node.neighbors.append(mapping[neighbor]) 
                

                
                
#workking version
from lintcode import (
    UndirectedGraphNode,
)

"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""
import collections
class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode: #给了一个点 A 
        if not node:
            return None

        print("original location", node, node.label)
        nodes = self.find_nodes_by_bfs(node)
        print("after find_nodes_by_bfs", [n for n in nodes])
        mapping = self.copy_nodes(nodes)
        print("after copy_nodes keys", mapping.keys())
        print("after copy_nodes values", mapping.values())
        self.copy_edges(nodes, mapping)
        
        return mapping[node] #返回了一个点 A‘ （不需要返回所有点）
    
    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node]) 
        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor in visited: 
                    continue
                queue.append(neighbor)
                visited.add(neighbor) 
        return list(visited)
        
    def copy_nodes(self, nodes):
        mapping = {}   
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping

    def copy_edges(self, nodes, mapping):
        for node in nodes: #for old_point in all old_points
            new_node = mapping[node] #new_node = UndirectedGraphNode(node.label)
            print("new_node", new_node)
            for neighbor in node.neighbors:
                new_node.neighbors.append(mapping[neighbor]) #new_neighbor = UndirectedGraphNode(neighbor.label)

                
