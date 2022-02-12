class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #LeetCode DFS w soln by sjin6, time O(V+E), space O(V+E)
        graph = collections.defaultdict(list)
        for prereq in prerequisites:        
            a, b = prereq
            graph[b].append(a)
        
        state = [0] * numCourses #state == -1 processing, state = 1 visited
        def isCycle(node: int) -> bool: #DFS
            if state[node] == -1:
                return True #there is a cycle
            if state[node] == 1:
                return False #already visited it and its descendants
            
            state[node] = -1
            for nextNode in graph[node]:
                if isCycle(nextNode):
                    return True
            state[node] = 1
            return False
        
        for course in range(numCourses):
            if isCycle(course):
                return False
        return True
        
#         #First attempt, topological sort on DAG, time O(V+E), space O(V+E)
#         graph = collections.defaultdict(list)
#         indegree = [0] * numCourses
#         for prereq in prerequisites:
#             a, b = prereq
#             graph[b].append(a)
#             indegree[a] += 1
        
#         queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
#         courseList = []
#         while queue:
#             course = queue.pop()
#             courseList.append(course)
            
#             for nextCourse in graph[course]:
#                 indegree[nextCourse] -= 1
#                 if indegree[nextCourse] == 0:
#                     queue.append(nextCourse)
#         return len(courseList) == numCourses
