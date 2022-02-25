class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(set)
        edge_weights = {}
        for u,v,cost in flights:
            graph[u].add(v)
            edge_weights[(u,v)] = cost
        
        #LeetCode DFS w/ DP and memo
        memo = {}
        def dfs(node, stops):
            if node == dst:
                return 0
            
            if stops < 0:
                return float('inf')
            
            if (node, stops) in memo:
                return memo[(node, stops)]
            
            ans = float('inf')
            for ngh in graph[node]:
                if (node, ngh) in edge_weights:
                    ans = min(ans, dfs(ngh, stops-1)+ edge_weights[(node, ngh)])
            memo[(node, stops)] = ans
            return ans
        
        res = dfs(src, k)
        return -1 if res == float('inf') else res
            
        #First attempt DFS - LTE
#         seen = {} #key: node, values: tuple(cost, stops)
#         def dfs(node, stops=0, cost=0):
#             if stops > k:
#                 return
            
#             if node == dst:
#                 if dst in seen:
#                     seen[dst][0] = min(seen[dst][0], cost)
#                 else:
#                     seen[dst] = [cost,stops]
#                 return
            
#             if node in seen:
#                 if seen[node][0] <= cost and seen[node][1] <= stops:
#                     return
#             seen[node] = [cost, stops]
            
#             for ngh in graph[node]:
#                 if ngh != dst:
#                     dfs(ngh, stops+1, cost+edge_weights[(node, ngh)])
#                 else:
#                     dfs(ngh, stops, cost+edge_weights[(node, ngh)])
#         dfs(src)
#         return seen[dst][0] if dst in seen else -1
