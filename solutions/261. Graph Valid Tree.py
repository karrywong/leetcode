class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n #size of each set
        
    def find(self, A: int) -> int: #Path Compression
        if A == self.parent[A]:
            return A
        self.parent[A] = self.find(self.parent[A])
        return self.parent[A]
    
    def union(self, A: int, B: int) -> bool:
        rootA = self.find(A)
        rootB = self.find(B)
        if rootA == rootB:
            return False
        if self.rank[rootA] <= self.rank[rootB]:
            self.parent[rootA] = rootB
            self.rank[rootB] += self.rank[rootA]
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += self.rank[rootB]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        unionFind = UnionFind(n)
        for A,B in edges:
            if not unionFind.union(A,B):
                return False
        return True
        
#         #eg1 adjList = [[1,2,3], [0,4], [0], [0], [1]]
#         #eg2 adjList = [[1], [0,2,4], [1,3], [1,2], [1]]
#         #DFS, detect cycle
#         #Time O(V+E), space O(V+E)
#         if len(edges) != n-1: 
#             return False
        
#         adjList = [[] for _ in range(n)]
#         for edge in edges:
#             v1, v2 = edge
#             adjList[v1].append(v2)
#             adjList[v2].append(v1)
        
# #         # soln 1 - recursive
# #         seen = set()
# #         def dfs(prev: int, cur: int) -> bool:
# #             seen.add(cur)
# #             for nextNode in adjList[cur]:
# #                 if nextNode == prev:
# #                     continue
# #                 if nextNode in seen or not dfs(cur, nextNode):
# #                     return False
# #             return True        
# #         return dfs(None,0) and len(seen) == n
        
#         #soln 2 - iterative
#         stack = [0]
#         parent = {0:-1}
#         while stack:
#             node = stack.pop()
#             for ngh in adjList[node]:
#                 if parent[node] == ngh:
#                     continue
#                 if ngh in parent:
#                     return False
#                 stack.append(ngh)
#                 parent[ngh] = node
#         return len(parent) == n
