class Solution:
    white = 1
    gray = 2
    black = 3
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Standard textbook topological sort using DFS, color vertices White, Gray, or Black
        #LeetCode implementation, time O(V+E), space O(V+E)
        graph = collections.defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)
            
        ans = []
        isPossible = True
        color = {k: Solution.white for k in range(numCourses)}
        def dfs(node):
            nonlocal isPossible
            if color[node] == Solution.black:
                return 
            if color[node] == Solution.gray:
                isPossible = False
                return
            
            color[node] = Solution.gray
            for nextNode in graph[node]:
                dfs(nextNode)
            color[node] = Solution.black
            ans.append(node)
            
        for course in range(numCourses):
            if color[course] == Solution.white:
                dfs(course)
        return ans[::-1] if isPossible else []
        
#         #First attempt in failed mock interview, had not yet learned topological sort
#         #Second attempt after reading CLRS book section 22.4 on topological sort, time O(V+E), space O(V+E)
#         graph = collections.defaultdict(list)
#         indegree = [0]*numCourses
#         for prereq in prerequisites:
#             a, b  = prereq
#             graph[b].append(a)
#             indegree[a] += 1
        
#         queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
#         ans = []
#         while queue:
#             course = queue.pop()
#             ans.append(course)
            
#             for nextCourse in graph[course]:
#                 indegree[nextCourse] -= 1
#                 if indegree[nextCourse] == 0:
#                     queue.append(nextCourse)
#         return ans if len(ans) == numCourses else []
