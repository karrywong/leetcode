class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, rootx, rooty):
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
​
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Minimum Spanning tree, Kruskal algorithm using union-find, time O(ElogE) due to sorting
        lookup = {i:(x,y) for i, (x,y) in enumerate(points)}
        edge_weights = []
        n = len(points)
        for i in range(n):
            for j in range(i):
                dist = abs(lookup[i][0]-lookup[j][0]) + abs(lookup[i][1]-lookup[j][1])
                edge_weights.append((dist, i, j))
        edge_weights.sort(reverse=True)
        count = n-1
        ans = 0
        uf = UnionFind(n)
        
        while count:
            edge_weight, u, v = edge_weights.pop()
            rootu = uf.find(u)
            rootv = uf.find(v)
            if rootu != rootv:
                uf.union(rootu,rootv)
                ans += edge_weight 
                count -= 1
                
        return ans
