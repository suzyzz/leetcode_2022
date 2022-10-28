# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.



# BFS - Topological Sorting O(V + E)	写出关答

import collections
class Solution
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        graph, in_degree = {i:[] for i in range(num_courses)}, [0] * num_courses
        order, queue = [], collections.deque([])
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            in_degree[pair[0]] += 1
        for i in range(num_courses):
            if in_degree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.popleft()
            order.append(course)
            print(graph[course])
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return True if len(order) == num_courses else False
