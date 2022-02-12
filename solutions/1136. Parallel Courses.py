class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        #First attempt, topological sort using Kahn, time O(V+E), space O(V+E)
        graph = collections.defaultdict(list)
        indegree = [0] * n
        for src, dest in relations:
            graph[src-1].append(dest-1)
            indegree[dest-1] += 1
        
        queue = collections.deque()
        numSemester = [0] * n
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                numSemester[i] = 1
        count = 0
        while queue:
            course = queue.pop()
            
            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1
                numSemester[nextCourse] = max(numSemester[nextCourse], numSemester[course]+1)
                if indegree[nextCourse] == 0 :
                    queue.append(nextCourse)      
            count += 1
            
        return max(numSemester) if count == n else -1
