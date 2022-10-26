# Description
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
# Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.


# 1.There is only one ball and one destination in the maze.
# 2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# 3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# 4.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

# Example
# Example 1:
# 	Input:  
# 	(rowStart, colStart) = (0,4)
# 	(rowDest, colDest)= (4,4)
# 	0 0 1 0 0
# 	0 0 0 0 0
# 	0 0 0 1 0
# 	1 1 0 1 1
# 	0 0 0 0 0

# 	Output:  12
	
# 	Explanation:
# 	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)

# Example 2:
# 	Input:
# 	(rowStart, colStart) = (0,4)
# 	(rowDest, colDest)= (0,0)
# 	0 0 1 0 0
# 	0 0 0 0 0
# 	0 0 0 1 0
# 	1 1 0 1 1
# 	0 0 0 0 0

# 	Output:  6
	
# 	Explanation:
# 	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(0,0)


# BFS

import collections

DIRECTIONS = {
    'U': [0, -1],
    'R': [1, 0],
    'D': [0, 1],
    'L': [-1, 0]
}

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        queue = collections.deque()
        distance = {}
        start = (start[0], start[1], None)
        destination = (destination[0], destination[1], None)

        queue.append(start)
        distance[start] = 0

        while queue:
            (curr_x, curr_y, curr_dire) = queue.popleft()
            if (curr_x, curr_y, curr_dire) == destination:
                return distance[(curr_x, curr_y, curr_dire)]

            if curr_dire != None:
                new_dire = curr_dire
                new_x, new_y = curr_x + DIRECTIONS[new_dire][0], curr_y + DIRECTIONS[new_dire][1]
                # is vaild -> 按当前方向走
                # not vaild -> 方向改成 None 
                if self.is_vaild(maze, new_x, new_y):
                    if (new_x, new_y, new_dire) in distance:
                        continue
                    queue.append((new_x, new_y, new_dire))
                    distance[(new_x, new_y, new_dire)] = distance[(curr_x, curr_y, curr_dire)] + 1
                else:
                    if (curr_x, curr_y, None) in distance:
                        continue
                    queue.append((curr_x, curr_y, None))
                    distance[(curr_x, curr_y, None)] = distance[(curr_x, curr_y, curr_dire)]
            else:
                for new_dire in DIRECTIONS:
                    new_x, new_y = curr_x + DIRECTIONS[new_dire][0], curr_y + DIRECTIONS[new_dire][1]
                    if self.is_vaild(maze, new_x, new_y):
                        if (new_x, new_y, new_dire) in distance:
                            continue
                        queue.append((new_x, new_y, new_dire))
                        distance[(new_x, new_y, new_dire)] = distance[(curr_x, curr_y, curr_dire)] + 1
        return -1
    
    def is_vaild(self, maze, x, y):
        n, m = len(maze), len(maze[0])
        if x < 0 or x >= n:
            return False
        if y < 0 or y >= m:
            return False
        return not maze[x][y]
	
