        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
#         #First attempt using Union Find, time O(len(equations)), space O(1)
#         #loop over equations and process only equal, call union(a,b)
#         #loop over equations and process only unequal, call find, if find(a) == find(b): return False
        
#         uf = UnionFind()
#         for equation in equations:
#             if equation[1] == "=":
#                 u = ord(equation[0]) - ord('a')
#                 v = ord(equation[3]) - ord('a')
#                 uf.union(u,v)
        
#         for equation in equations:
#             if equation[1] == "!":        
#                 u = ord(equation[0]) - ord('a')
#                 v = ord(equation[3]) - ord('a')
#                 if uf.find(u) == uf.find(v):
#                     return False
#         return True
​
        #Second attempt using DFS, time O(len(equations)), space O(len(equations))
        graph = collections.defaultdict(set)
        for equation in equations:
            if equation[1] == "=":
                u = ord(equation[0]) - ord('a')
                v = ord(equation[3]) - ord('a')
                graph[u].add(v)
                graph[v].add(u)
        
        colors = [None] * 26
        cnt = 0
        
        def dfs(node: int, cnt: int):
            colors[node] = cnt
            for ngh in graph[node]:
                if colors[ngh] is None:
                    dfs(ngh, cnt)
        
        for i in range(26):
            if colors[i] is None:
                dfs(i, cnt)
                cnt += 1
        
        for equation in equations:
            if equation[1] == "!":
                u = ord(equation[0]) - ord('a')
                v = ord(equation[3]) - ord('a')
                if colors[u] == colors[v]:
                    return False
        return True
