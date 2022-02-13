# class UnionFind:
#     def __init__(self, n: int):
#         self.parent = [i for i in range(n)]
#         self.rank = [1]*n #size of each set
#         self.count = n
        
#     def find(self, A: int) -> int: #Path Compression
#         if A == self.parent[A]:
#             return A
#         self.parent[A] = self.find(self.parent[A])
#         return self.parent[A]
    
#     def union(self, A, B):
#         rootA = self.find(A)
#         rootB = self.find(B)
#         if rootA != rootB:
#             if self.rank[rootA] >= self.rank[rootB]:
#                 self.parent[rootA] = rootB
#                 self.rank[rootA] += self.rank[rootB]
#             else:
#                 self.parent[rootB] = rootA
#                 self.rank[rootB] += self.rank[rootA]
#             self.count -= 1
            
#     def getCount(self):
#         return self.count
​
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # unionFind = UnionFind(n)
        # for A, B in edges:
        #     unionFind.union(A,B)
        # return unionFind.getCount()
        
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        count = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                stack = [i]
                while stack:
                    node = stack.pop()
                    seen.add(node)
                    for nextNode in graph[node]:
                        if nextNode not in seen:
                            stack.append(nextNode)
                
                count += 1
        return count
