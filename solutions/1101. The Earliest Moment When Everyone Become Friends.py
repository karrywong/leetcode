class UnionFind:
    def __init__(self, n:int):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
        self.count = n
    
    def find(self, x:int) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x:int, y:int):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1
        
    def get_count(self):
        return self.count
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        for time, a, b in sorted(logs):
            uf.union(a,b)
            if uf.get_count() == 1:
                return time
        return -1
