# class UnionFind:
#     def __init__(self, n:int):
#         self.parent = [i for i in range(n)]
#         self.rank = [1] * n
    
#     def find(self, x:int) -> int:
#         if x == self.parent[x]:
#             return x
#         self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
    
#     def union(self, x:int, y:int):
#         rootx = self.find(x)
#         rooty = self.find(y)
#         if rootx != rooty:
#             if self.rank[rootx] < self.rank[rooty]:
#                 self.parent[rootx] = rooty
#             elif self.rank[rootx] > self.rank[rooty]:
#                 self.parent[rooty] = rootx
#             else:
#                 self.parent[rooty] = rootx
#                 self.rank[rootx] += 1
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #Soln 1 DFS - Time O(E+VlogV), space O(E+V)
        def dfs(v:int) -> None:
            visited.add(v)
            indices.append(v)
            for ngh in adjList[v]:
                if ngh not in visited:
                    dfs(ngh)
        
        n = len(s)
        adjList = collections.defaultdict(set)
        for i, j in pairs:
            adjList[i].add(j)
            adjList[j].add(i)
            
        visited = set()
        ans = [None for _ in range(n)]
        for i in range(n):
            if i not in visited:
                indices = []
                dfs(i)
                letters = [s[k] for k in indices]
                for ind, char in zip(sorted(indices), sorted(letters)):
                    ans[ind] = char
        return ''.join(ans)
        
#         #Soln 2 - Time O((E+V)*\alpha(V)+VlogV), space O(V)
#         n = len(s)
#         uf = UnionFind(n)
#         for a,b in pairs:
#             uf.union(a,b)
            
#         letters = collections.defaultdict(list)
#         indices = collections.defaultdict(list)
#         for i in range(n):
#             indices[uf.find(i)].append(i)
#             letters[uf.find(i)].append(s[i])
#         # print(indices, letters)
        
#         ans = [None] * n
#         for k in set(uf.parent):
#             for ind, char in zip(indices[k], sorted(letters[k])):
#                 ans[ind] = char
#         # print(ans)
#         return ''.join(ans)
