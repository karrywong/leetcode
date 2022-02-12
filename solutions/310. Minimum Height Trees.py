class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:    
        #LeetCode topological sort, clever, idea is to find centroids nodes (always less or equal to two)
        #stepwise trim nodes that are furthest away from centroids until two or one nodes are left        
        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
            
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        while len(graph) > 2:
            newLeaves = []
            while leaves:
                leaf = leaves.pop()
                ngh = graph[leaf].pop()
                graph[ngh].remove(leaf)
                if len(graph[ngh]) == 1:
                    newLeaves.append(ngh)
                del graph[leaf]
            leaves = newLeaves
        return graph.keys()
            
#         #First attempt w DFS, TLE, time O(N^2), space O(N), where N=n is number of nodes
#         graph = collections.defaultdict(list)
#         for v1, v2 in edges:
#             graph[v1].append(v2)
#             graph[v2].append(v1)
        
#         memo = {}
#         def dfs(prev, cur) -> int:
#             if len(graph[cur]) == 1 and graph[cur][0] == prev:
#                 return 0
#             if (prev, cur) in memo:
#                 return memo[(prev, cur)]
            
#             height = 0
#             for child in graph[cur]:
#                 if child == prev:
#                     continue
#                 height = max(height, dfs(cur, child)+1)
#             memo[(prev, cur)] = height
#             return height
        
#         heights = {}
#         mhtHeight = n
#         for i in range(n):
#             heights[i] = dfs(None, i)
#             mhtHeight = min(mhtHeight, heights[i])
        
#         return [i for i in heights if heights[i] == mhtHeight]
