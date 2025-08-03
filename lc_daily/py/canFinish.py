from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            course = queue.pop(0)
            count += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return count == numCourses


sln = Solution()
print(sln.canFinish(2,[[1,0]]))