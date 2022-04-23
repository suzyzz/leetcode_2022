# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 
# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

#Method 1: BFS 单列对
import collections

class Solution:
        def findCircleNum(self, M):
            ansbfs = self.beginbfs(M)
            return ansbfs
        
        def beginbfs(self, M):
            n = len(M)
            ans = 0
            visisted = {} # 标记是否访问过            
            for i in range(n):
                visisted[i] = False

            # 遍历每个人，如果这个人还没访问过 就从这个人开始做一遍bfs
            for i in range(n):
                if (visisted[i] == False):      # 这个人还没访问过
                    ans += 1                    # 答案+1
                    q = collections.deque()     # 初始化一个列队
                    visisted[i] = True          # 标记起点并压入队列，这里避免了m[i][i] = 1
                    q.append(i)
                    while (len(q) != 0):        # 把从i开始的所有相关朋友找完
                        now = q.popleft()       # 取出队首 作为开始                 
                        for j in range(n):      # 从队首找朋友
                            if (M[now][j] == 1 and visisted[j] == False): # 找到新朋友
                                visisted[j] = True # 标记访问
                                q.append(j)     # 压入队列
            return ans
