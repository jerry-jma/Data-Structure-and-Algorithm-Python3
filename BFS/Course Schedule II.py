# Description
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Wechat reply the 【616】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

# Example
# Example 1:

# Input: n = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Example 2:

# Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # in degree
        in_degree = {x: 0 for x in range(numCourses)}
        course_neighbors = {x: [] for x in range(numCourses)}

        for after_prereq, prereq in prerequisites:
            course_neighbors[prereq].append(after_prereq)
            in_degree[after_prereq] += 1

        queue = collections.deque()
        topo_order = []
        for x in in_degree:
            if in_degree[x] == 0:
                queue.append(x)

        while queue:
            course = queue.popleft()
            topo_order.append(course)
            for after_prereq in course_neighbors[course]:
                in_degree[after_prereq] -= 1
                if in_degree[after_prereq] == 0:
                    queue.append(after_prereq)

        if len(topo_order) != numCourses:
            return []

        return topo_order




