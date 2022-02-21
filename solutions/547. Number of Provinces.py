class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
​
    def find(self, i): #Path Compression
        if self.parent[i] != i:
            return self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.parent[yroot] = xroot
            self.count -= 1
            
    def get_count(self):
        return self.count
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #Second attempt, Union Find, soln by crazyphotonzz
        #time O(N^3) with matrix tranversed once & union/find O(N) in worst case, space O(N)
        n = len(isConnected[0])
        uf = UnionFind(n) #Union-Find soln
        
        for r in range(n):
            for c in range(r+1, n):
                if isConnected[r][c] == 1:
                    uf.union(r,c)
        
        return uf.get_count()
        
        # #first attempt, iterative dfs + stack, time O(N^2), space O(N)
        # n = len(isConnected)
        # seen = set()
        # ans = 0
        # for i, row in enumerate(isConnected):
        #     if i in seen: continue
        #     for j in range(n):
        #         if j == i: continue
        #         if row[j] and j not in seen:
        #             stack = [j]
        #             seen.add(j)
        #             while stack:
        #                 idx = stack.pop()
        #                 for k in range(n):
        #                     if k == j: continue
        #                     if isConnected[idx][k] and k not in seen:
        #                         stack.append(k)
        #                         seen.add(k)
        #             ans += 1
        # return ans + (n-len(seen))
