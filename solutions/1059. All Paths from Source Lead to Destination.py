class Solution:
    gray = 1
    black = 2
    
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #Too many Failed attempts
        #Soln 2, DFS by cenkay, really clever, time O(V), space O(V+E)
        def dfs(i):
            seen.add(i)
            for j in graph[i]:
                if j == i or j in seen or not dfs(j):
                    return False
            seen.remove(i)
            return len(graph[i]) != 0 or i == destination
            
        graph, seen = collections.defaultdict(set), set()
        for a, b in edges:
            graph[a].add(b)
        return dfs(source)
        
#         #Soln 1 - LeetCode DFS, time O(V), space O(V+E)
#         graph = [[] for _ in range(n)]
#         for s,e in edges:
#             graph[s].append(e)
            
#         def leadsToDest(node, states = [None]*n):
#             if states[node] != None:
#                 return states[node] == Solution.black #if state is gray, found a cycle
            
#             if len(graph[node]) == 0:
#                 return node == destination #leaf node must be destination
            
#             states[node] = Solution.gray  # Now, we are processing this node. So we mark it as GRAY.
#             for nextNode in graph[node]:
#                 # If we get a `false` from any recursive call on the neighbors, we break and return False
#                 if not leadsToDest(nextNode, states):
#                     return False
#             states[node] = Solution.black # Recursive processing done for the node. We mark it BLACK.
#             return True
            
#         return leadsToDest(source)
