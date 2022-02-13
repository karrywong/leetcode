class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n #size of each set
        self.count = n
        
    def find(self, A: int) -> int: #Path Compression
        if A == self.parent[A]:
            return A
        self.parent[A] = self.find(self.parent[A])
        return self.parent[A]
    
    def union(self, A, B):
        rootA = self.find(A)
        rootB = self.find(B)
        if rootA != rootB:
            if self.rank[rootA] >= self.rank[rootB]:
                self.parent[rootA] = rootB
                self.rank[rootA] += self.rank[rootB]
            else:
                self.parent[rootB] = rootA
                self.rank[rootB] += self.rank[rootA]
            self.count -= 1
            
    def getCount(self):
        return self.count
​
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        for A, B in edges:
            unionFind.union(A,B)
        return unionFind.getCount()
        
        # #TBRV, soln by Zitao
        # dic = {}
        # for e in edges:
        #     if e[0] not in dic:
        #         dic[e[0]] = [e[1]]
        #     else:
        #         dic[e[0]].append(e[1])
        #     if e[1] not in dic:
        #         dic[e[1]] = [e[0]]
        #     else:
        #         dic[e[1]].append(e[0])
        # seen = [0]*n
        # count = 0
        # for i in range(n):
        #     if seen[i] == 0:
        #         count += 1
        #         stack = [i]
        #         while stack:
        #             u = stack.pop()
        #             seen[u] = 1
        #             if u in dic:
        #                 for neighbor in dic[u]:
        #                     if seen[neighbor] == 0:
        #                         stack.append(neighbor)
        # return count
