# Description
# On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
# Given an initial state of the puzzle board and final state, return the least number of moves required so that the initial state to final state.
# If it is impossible to move from initial state to final state, return -1.

# Example
# Example 1:

# Input:
# [
#  [2,8,3],
#  [1,0,4],
#  [7,6,5]
# ]
# [
#  [1,2,3],
#  [8,0,4],
#  [7,6,5]
# ]
# Output:
# 4

# Explanation:
# [                 [
#  [2,8,3],          [2,0,3],
#  [1,0,4],   -->    [1,8,4],
#  [7,6,5]           [7,6,5]
# ]                 ]

# [                 [
#  [2,0,3],          [0,2,3],
#  [1,8,4],   -->    [1,8,4],
#  [7,6,5]           [7,6,5]
# ]                 ]

# [                 [
#  [0,2,3],          [1,2,3],
#  [1,8,4],   -->    [0,8,4],
#  [7,6,5]           [7,6,5]
# ]                 ]

# [                 [
#  [1,2,3],          [1,2,3],
#  [0,8,4],   -->    [8,0,4],
#  [7,6,5]           [7,6,5]
# ]                 ]
# Example 2：

# Input:
# [[2,3,8],[7,0,5],[1,6,4]]
# [[1,2,3],[8,0,4],[7,6,5]]
# Output:
# -1
# Challenge
# How to optimize the memory?
# Can you solve it with A* algorithm?


# 通用BFS模板+转换matrix to string

from typing import (
    List,
)

from collections import deque 

DIRECTIONS = [
    (0, 1), (0, -1), (1, 0), (-1, 0)    
]

class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        init_state_str = self.matrixToList(init_state)
        final_state_str = self.matrixToList(final_state)
        
        if init_state_str == final_state_str:
            return 0
        
        visited = set([init_state_str])
        q = deque([init_state_str])
        count = 0
        while q:
            size = len(q)
            for _ in range(size): # find shortest distance
                node = q.popleft()
                if node == final_state_str:
                    return count
                neighbors = self.getNeighborMatrix(node)
                for nb in neighbors:
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
            count += 1
        return -1
    
    # list can't be used as key of tuple
    # transfer list to a string
    def matrixToList(self, matrix):
        seq = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                seq.append(str(matrix[i][j]))
        return "".join(seq)
    
    # get neighboring matrices
    def getNeighborMatrix(self, cur_state):
        zeroIndex = cur_state.index('0')
        x, y = zeroIndex // 3, zeroIndex % 3
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nIndex = nx * 3 + ny
                cur_state_list = list(cur_state)
                cur_state_list[zeroIndex], cur_state_list[nIndex] = cur_state_list[nIndex], cur_state_list[zeroIndex]
                neighbors.append(''.join(cur_state_list))
        return neighbors




