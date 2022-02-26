class UnionFind:
    def __init__(self):
        self.root = [i for i in range(26)]
        self.rank = [0]*26
        
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
                self.root[rootx] = rooty
                self.rank[rootx] += 1
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        #First attempt using Union Find, time O(N) w/ N = len(equations), space O(1)
        #loop over equations and process only equal, call union(a,b)
        #loop over equations and process only unequal, call find, if find(a) == find(b): return False
        
        uf = UnionFind()
        for equation in equations:
            if equation[1] == "=":
                u = ord(equation[0]) - ord('a')
                v = ord(equation[3]) - ord('a')
                uf.union(u,v)
        
        for equation in equations:
            if equation[1] == "!":        
                u = ord(equation[0]) - ord('a')
                v = ord(equation[3]) - ord('a')
                if uf.find(u) == uf.find(v):
                    return False
        return True
