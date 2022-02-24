#                 self.rank[rootx] += 1
#             self.count -= 1
            
#     def get_count(self):
#         return self.count
​
class Solution:    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # #Second attempt using Union Find, time O(N*alpha(N)), space O(N)
        # if len(connections) < n-1: 
        #     return -1
        # uf = UnionFind(n)
        # for u, v in connections:
        #     uf.union(u,v)
        # return uf.get_count()-1
                
#         #First attempt using DFS, time O(N+len(connections)), space O(N)
        if len(connections) < n-1: 
            return -1
        graph = collections.defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        
#         seen = set()
#         count = 0
#         def dfs(node):
#             if node in seen:
#                 return
#             seen.add(node)       
#             for ngh in graph[node]:
#                 if ngh not in seen:
#                     dfs(ngh)
            
#         for i in range(n):
#             if i not in seen:
#                 count += 1
#                 dfs(i)
#         return count-1
​
        #Third attempt using BFS,  time O(N+len(connections)), space O(N)
        seen = set()
        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                queue = collections.deque([i])
                seen.add(i)
                while queue:
                    node = queue.popleft()
                    for ngh in graph[node]:
                        if ngh not in seen:
                            queue.append(ngh)
                            seen.add(ngh)
        return count - 1
