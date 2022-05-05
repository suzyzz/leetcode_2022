# Description
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Example
# Example 1:

# Input: n = 2, prerequisites = [[1,0]] 
# Output: [0,1]
# Example 2:

# Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
# Output: [0,1,2,3] or [0,2,1,3]

#自己写的
import collections
class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def find_order(self, num_courses, prerequisites):
        graph = [[] for _ in range(num_courses)]
        in_degree = [0] * num_courses

        for course_in, course_out in prerequisites:
            graph[course_out].append(course_in)
            in_degree[course_in] += 1

        topo_order = []
        queue = collections.deque()
        for i in range(num_courses):
            if in_degree[i] == 0:
                queue.append(i)
            
        while queue:
            current_course = queue.popleft()
            topo_order.append(current_course)
            for next_course in graph[current_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course) 
        
        return topo_order if len(topo_order) == num_courses else []
      
      
      
#关答
from typing import (
    List,
)

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def find_order(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] += 1

        num_choose = 0
        queue = collections.deque()
        topo_order = []
        
        # 将入度为 0 的编号加入队列
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            now_pos = queue.popleft()
            topo_order.append(now_pos)
            num_choose += 1
            # 将每条邻边删去，如果入度降为 0，再加入队列
            for next_pos in graph[now_pos]:
                in_degree[next_pos] -= 1
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)
                
        
        if num_choose == numCourses:
            return topo_order
        return []
