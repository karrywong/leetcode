class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x): #path compression
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y): #union by rank
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
​
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        #Union-Find soln, time complexity O(requests * restrictions), space O(n)
        no_friend = collections.defaultdict(set)
        for u, v in restrictions:
            no_friend[u].add(v)
            no_friend[v].add(u)
          
        ans = []
        uf = UnionFind(n)
        for u, v in requests:
            rootu = uf.find(u)
            rootv = uf.find(v)
            
            approved = True
            #Check if same root
            if rootu == rootv:
                ans.append(approved)
                continue
            
            #Check each restriction
            for x, y in restrictions:
                rootx, rooty = uf.find(x), uf.find(y)
                if (rootu, rootv) == (rootx, rooty) or (rootu, rootv) == (rooty, rootx):
                    approved = False
                    break            
            
            #Not same root
            if approved:
                uf.union(u,v)
            ans.append(approved)
        return ans
