class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        #A conceptually very similar problem, 997. Find the Town Judge
        #Don't rush into graph related structures like adjacency list, etc.
        
        #Second attempt, better
        ans = set([i for i in range(n)])
        for edge in edges:
            if edge[1] in ans:
                ans.remove(edge[1])
        return list(ans)
        
        #First attempt, key - find nodes with zero incoming edges
        # inedges = collections.defaultdict(int)
        # for edge in edges:
        #     inedges[edge[1]] += 1
        # ans = set([i for i in range(n)])
        # return list(ans.difference(inedges.keys()))
        
        
        
