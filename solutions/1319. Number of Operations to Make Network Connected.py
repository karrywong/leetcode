class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n
        self.count = n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            elif self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1
            
    def get_count(self):
        return self.count
​
class Solution:    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #Second attempt using Union Find, time O(N*alpha(N)), space O(N)
        if len(connections) < n-1: 
            return -1
        uf = UnionFind(n)
        for u, v in connections:
            uf.union(u,v)
        return uf.get_count()-1
        
#         #First attempt using DFS, time O(N+len(connections)), space O(N)
#         if len(connections) < n-1: 
#             return -1
#         graph = collections.defaultdict(set)
#         for u, v in connections:
#             graph[u].add(v)
#             graph[v].add(u)
        
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
