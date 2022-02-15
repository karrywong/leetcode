class UnionFind:
    def __init__(self, n:int):
        self.root = [i for i in range(n)]
    
    def find(self, x:int) -> int: #path compression
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x:int, y:int):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == 0:
            rootx, rooty = rooty, rootx
        self.root[rootx] = rooty
        
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        #Idea from RJMCMC how to deal with simultaneous meetings
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        
        time_store = collections.defaultdict(list)
        for x,y,t in meetings:
            time_store[t].append((x,y))
            
        for time in sorted(time_store):
            intermediate_seen = set()
            for x,y in time_store[time]:
                uf.union(x,y)
                intermediate_seen.add(x)
                intermediate_seen.add(y)
            
            for val in intermediate_seen:
                uf.find(val)
                if  uf.root[val] != 0:
                    uf.root[val] = val
        return [i for i in range(n) if uf.find(i) == 0]
​
