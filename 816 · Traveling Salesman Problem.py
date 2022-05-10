# Description
# Give n cities(labeled from 1 to n), and the undirected road's cost among the cities as a three-tuple [A, B, c](i.e there is a road between city A and city B and the cost is c). We need to find the smallest cost to travel all the cities starting from 1.

# 1.A city can only be passed once.
# 2.You can assume that you can reach all the rest cities.

# Example
# Example 1

# Input: 
# n = 3
# tuple = [[1,2,1],[2,3,2],[1,3,3]]
# Output: 3
# Explanation: The shortest path is 1->2->3
# Example 2

# Input:
# n = 1
# tuple = []
# Output: 0

#关答 1： 暴力 DFS 算法
class Result:
    def __init__(self):
        self.min_cost = float('inf')
    
class Solution:
    def min_cost(self, n, roads):
        graph = self.construct_graph(roads, n)
        result = Result()
        self.dfs(1, n, set([1]), 0, graph, result)
        return result.min_cost
        
    def dfs(self, city, n, visited, cost, graph, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return
    
        for next_city in graph[city]:
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(next_city, n, visited, cost + graph[city][next_city], graph, result)
            visited.remove(next_city)
    
    def construct_graph(self, roads, n):
        graph = {i: {} for i in range(1, n + 1)}
        for a, b, c in roads:
            if b not in graph[a]:
                graph[a][b] = c
            else:
                graph[a][b] = min(graph[a][b], c)
            if a not in graph[b]:
                graph[b][a] = c
            else:
                graph[b][a] = min(graph[b][a], c)
        return graph
      
      
      
#暴力剪枝      
class Result:
    def __init__(self):
        self.min_cost = float('inf')
    
class Solution:
    def minCost(self, n, roads):
        graph = self.construct_graph(roads, n)
        result = Result()
        self.dfs(1, n, [1], set([1]), 0, graph, result)
        return result.min_cost
        
    def dfs(self, city, n, path, visited, cost, graph, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return
    
        for next_city in graph[city]:
            if next_city in visited:
                continue
            if self.has_better_path(graph, path, next_city):
                continue
            visited.add(next_city)
            path.append(next_city)
            self.dfs(next_city, n, path, visited, cost + graph[city][next_city], graph, result)
            path.pop()
            visited.remove(next_city)
    
    def construct_graph(self, roads, n):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
        return graph
        
    def has_better_path(self, graph, path, city):
        for i in range(1, len(path)):
            if graph[path[i - 1]][path[i]] + graph[path[-1]][city] >\
                    graph[path[i - 1]][path[-1]] + graph[path[i]][city]:
                return True
        return False


        
