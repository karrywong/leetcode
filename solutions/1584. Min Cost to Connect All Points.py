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
#         #Soln 1 - MST, Kruskal algorithm using union-find, time O(ElogV) due to sorting
#         edge_weights = []
#         n = len(points)
#         for i in range(n):
#             for j in range(i):
#                 dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
#                 edge_weights.append((dist, i, j))
#         edge_weights.sort(reverse=True)
#         count = n-1
#         ans = 0
#         uf = UnionFind(n)
        
#         while edge_weights and count:
#             edge_weight, u, v = edge_weights.pop()
#             rootu = uf.find(u)
#             rootv = uf.find(v)
#             if rootu != rootv:
#                 uf.union(rootu,rootv)
#                 ans += edge_weight 
#                 count -= 1
#         return ans
​
        #Soln 2 - MST, Prim's algorithm using heap, time O(ElogV)
        n = len(points)
        hp = []
        visited = set()
        x1, y1 = points[0]
        for i in range(1, n):
            dist = abs(points[i][0] - x1) + abs(points[i][1]-y1)
            hp.append((dist, 0, i))
        heapq.heapify(hp)
        visited.add(0)
        
        ans = 0
        count = n-1
        while hp and count:
            cost, u, v = heapq.heappop(hp)
            if v not in visited:
                x1, y1 = points[v]
                ans += cost
                visited.add(v)
                for i in range(n):
                    if i not in visited:
                        dist = abs(points[i][0] - x1) + abs(points[i][1]-y1)
                        heapq.heappush(hp, (dist, v, i))
                count -= 1
        return ans
