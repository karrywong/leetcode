class Solution:
    white = 0
    gray = 1
    black = 2
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #Too many faild attempts, eventually the right idea but failed to implement
        #1st scan: [[1,2],[2,3],[5],[0],[5],[],[]] -> queue = [5,6]
        #rgraph = [[3], [0], [0,1], [1], [], [2,4], []] -> queue = [2,4]
        #2nd scan: [[1,2],[2,3],[],[0],[],[],[]] -> ans = [2,4]
        #soln 1 - Leetcode reverse edges, time O(N+E), space O(N)
#         n = len(graph)
#         safe = [False] * n
        
#         graph = list(map(set, graph))
#         rgraph = collections.defaultdict(set)
#         queue = collections.deque()
        
#         for node, edges in enumerate(graph):
#             if not edges:
#                 queue.append(node)
#             for edge in edges:
#                 rgraph[edge].add(node)
                
#         while queue:
#             node = queue.popleft()
#             safe[node] = True
#             for nextNode in rgraph[node]:
#                 graph[nextNode].remove(node)
#                 if len(graph[nextNode]) == 0:
#                     queue.append(nextNode)
#         return [node for node, bo in enumerate(safe) if bo]
    
        #soln 2 - Textbook recursive DFS
        n = len(graph)
        states = [Solution.white] * n
        ans = []
        def dfs(node):
            if states[node] != Solution.white:
                return states[node] == Solution.black
            
            states[node] = Solution.gray
            for ngh in graph[node]:
                if states[ngh] == Solution.black:
                    continue
                if states[ngh] == Solution.gray or not dfs(ngh):
                    return False
            states[node] = Solution.black
            return True
        return [i for i in range(n) if dfs(i)]
