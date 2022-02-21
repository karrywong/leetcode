class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)] #0, 1 to n
        self.rank = [1] * (n+1)
    
    def find(self, x): #path compression
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y): #union by rank
        rootx = self.find(x)
        rooty = self.find(y)
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
    
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        #First attempt, Prim's algorithm, time #O(N*log(N)), N = len(connections)
        #data structure: heap, starting point = 1
        graph = collections.defaultdict(list)
        for city1, city2, cost in connections:
            graph[city1].append((cost, city2))
            graph[city2].append((cost, city1))
​
        hp = graph[1]
        heapq.heapify(hp)
        visited = set([1])
​
        min_cost = 0
        while hp:
            cost, next_city = heapq.heappop(hp)
            if next_city not in visited:
                min_cost += cost
                visited.add(next_city)
                for new_cost, new_city in graph[next_city]:
                    if new_city not in visited:
                        heapq.heappush(hp, (new_cost, new_city))
        return min_cost if len(visited) == n else -1       
​
#         #second attempt, Krushal's algorithm, time #O(N*log(N)), N = len(connections)
#         edge_weights = [] #(cost, i, j)
#         for i, j, cost in connections:
#             edge_weights.append((cost, i, j))
        
#         edge_weights.sort(reverse = True) 
#         count = n-1
#         min_cost = 0
#         uf = UnionFind(n)
        
#         while edge_weights and count:
#             cost, i, j = edge_weights.pop()
#             if uf.find(i) != uf.find(j):
#                 uf.union(i,j)
#                 min_cost += cost
#                 count -=1
        
#         return min_cost if count == 0 else -1
