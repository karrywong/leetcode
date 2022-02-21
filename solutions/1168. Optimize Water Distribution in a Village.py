class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        #Modified MST by adding imginary pt 0 for building the well, from 0 to n, (n+1) points
        #Prim's algorithm using heap, time O((N+M)*log(N+M)), space O(N+M)
        edge_weights = {}
        adjList = collections.defaultdict(set)
        
        hp = []
        visited = set()
        for i in range(n):
            hp.append((wells[i], 0, i+1))
            adjList[0].add(i+1)
            adjList[i+1].add(0)
            edge_weights[(0,i+1)] = wells[i]
        heapq.heapify(hp)
        visited.add(0)
        
        for i, j, cost in pipes:
            adjList[i].add(j)
            adjList[j].add(i)
            if i > j:
                i,j = j,i 
            if (i,j) in edge_weights:
                edge_weights[(i,j)] = min(edge_weights[(i,j)], cost)
            else:
                edge_weights[(i,j)] = cost
        
        ans = 0
        count = n+1
        while hp and count:
            cost, u, v = heapq.heappop(hp)
            if v not in visited:
                ans += cost
                visited.add(v)
                for ngh in adjList[v]:
                    if ngh not in visited:
                        cost = edge_weights[(ngh, v)] if ngh < v else edge_weights[(v, ngh)]
                        heapq.heappush(hp, (cost, v, ngh))
                count -= 1
        return ans
