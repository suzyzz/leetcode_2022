# Description
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example
# Example 1:
# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.
# Example 2:
# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.

# *******************说明********************
# 图是树的条件：
# 1. 连贯
# 2. 边必须有n-1个
# 3. 没有环
# *****任意两个条件满足 => 是树


# BFS - O(max(n, m)) 用条件1，2
from typing import (
    List,
)
import collections
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        numOfEdge = len(edges)
        # 判断是否为 (n - 1) 条边
        if numOfEdge != n - 1:
            return False
        # adjacent[i]里存i的相邻点
        adjacent = [[0] * n for _ in range(n)] 
        for i in range(numOfEdge):
            u = edges[i][0]
            v = edges[i][1]
            adjacent[u][v] = adjacent[v][u] = 1
        print(adjacent)
        # visit[i]记录i是否被访问
        visit = [0] * n
        # 0作为根结点，开始向下遍历
        visit[0] = 1
        root, numOfVisited = 0, 1
        q = collections.deque()
        q.append(root)
        while len(q) != 0:
            root = q.popleft()
            for i in range(n):
                if adjacent[root][i] != 1:
                    continue
                # 如果相邻且没有被访问过，说明是儿子，加入队列
                if visit[i] == 0:
                    visit[i] = 1
                    numOfVisited += 1
                    q.append(i)
        if numOfVisited == n:
            return True
        return False

      
      
#      并查集 - O(M Alpha(N))，这里Alpha是Ackerman函数的某个反函数 用条件2，3
from typing import (
    List,
)
import collections
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """        
    def valid_tree(self, n, edges):
        # write your code here
        # 初始化pre数组，每个节点的根节点都是自己
        pre = [i for i in range(n)]
        for i in edges:
            root_u = self.find_root(pre, i[0])
            root_v = self.find_root(pre, i[1])
            # 如果成环则不是树
            if root_u == root_v: 
                return False
            else:
                pre[root_u] = root_v
        # 统计根节点数目来判断是否连通
        cnt = 0
        for i in range(n):
            if self.find_root(pre, i) == i:
                cnt += 1 
        return cnt == 1

    def find_root(self, pre, x):
        # 找到根结点
        root = x
        while root != pre[root]:
            root = pre[root]
        # 路径压缩
        while x != pre[x]:
            x, pre[x] = pre[x], root;
        return root
