class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         #Soln 4 - Bellman-Ford algorithm using a DP approach, time O(k*E), space O(V)
#         prev = [float('inf')] * n
#         cur = [float('inf')] * n
#         prev[src] = 0
        
#         for i in range(1,k+2):
#             cur[src] = 0
#             for u,v,cost in flights:
#                 if prev[u] < float('inf'):
#                     cur[v] = min(cur[v], prev[u]+cost)
#             prev = cur[:]
#         return -1 if cur[dst] == float('inf') else cur[dst]
​
#         # #Adjacency list for solns 1 -3 
        graph = collections.defaultdict(set)
        edge_weights = {}
        for u,v,cost in flights:
            graph[u].add(v)
            edge_weights[(u,v)] = cost
        
#         #Soln 3 - Modified Dijstra's Algorithm, time O(ElogV), space O(E)
        costs = [float("inf") for _ in range(n)]
        stops_count = [float("inf") for _ in range(n)]
        
        hp = [(0,0,src)]
        heapq.heapify(hp)
        while hp:
            cost, stops, node = heapq.heappop(hp)
            if node == dst:
                return cost
            
            if stops == k+1:
                continue
            
            costs[node] = cost
            stops_count[node] = stops
            
            for ngh in graph[node]:
                edge_weight = edge_weights[(node, ngh)]
                #if better cost, add into heap
                #or if fewer stops, add into heap
                if cost + edge_weight < costs[ngh] or stops+1 < stops_count[ngh]: 
                    heapq.heappush(hp, (cost + edge_weight, stops+1, ngh))
        # return -1 if costs[dst] == float("inf") else costs[dst]
        return -1
        
#         #Soln 2 - LeetCode DFS w/ DP and memo, time O(V+E), space O(E)
#         memo = {}
#         def dfs(node, stops):
#             if node == dst:
#                 return 0
            
#             if stops < 0:
#                 return float('inf')
            
#             if (node, stops) in memo:
#                 return memo[(node, stops)]
            
#             ans = float('inf')
#             for ngh in graph[node]:
#                 if (node, ngh) in edge_weights:
#                     ans = min(ans, dfs(ngh, stops-1)+ edge_weights[(node, ngh)])
#             memo[(node, stops)] = ans
#             return ans
        
#         res = dfs(src, k)
#         return -1 if res == float('inf') else res
            
