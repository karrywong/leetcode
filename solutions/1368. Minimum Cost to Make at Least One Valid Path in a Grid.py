class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        #Soln 2 - follow hints to use BFS and update queue by DFS (greedy), clean implementation by lee215
        #Key observation - We will never detour the path to a node that we can already reach
        #Time: O(MN), space O(MN)
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        dist = 0
        queue = []
        
        def dfs(i: int, j: int):
            if not (0 <= i < m and 0 <= j < n and dp[i][j] == float('inf')):
                return
            dp[i][j] = dist
            queue.append((i,j))
            di, dj = moves[grid[i][j]-1]
            dfs(i+di, j+dj)
        
        dfs(0,0)
        while queue:
            dist += 1
            queue, queue_prev = [], queue
            for k in range(len(queue_prev)):
                x,y = queue_prev[k]
                for h in range(4):
                    dx,dy = moves[h][0], moves[h][1]
                    dfs(x+dx,y+dy)
        
        return dp[-1][-1]
    
#         #Soln 1 - Single source shortest path, Dijkstra's algorithm, inspired by abhijeet22's soln
#         #Drawback is duplicate coordinates in heap, since no efficient way to update priority
#         #Time O(ElogV) w/ E = O(4MN), V = O(MN), space O(MN)
#         m, n = len(grid), len(grid[0])
#         hp = [(0,0,0)] #(dist,i,j)
#         heapq.heapify(hp)
#         distances = {(0,0): 0} #key:(i,j), value:distance
#         moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
#         while hp:
#             dist, x, y = heapq.heappop(hp)
#             # print(x,y,distances)
#             # print(hp)
#             if x == m-1 and y == n-1:
#                 return dist
            
#             for i in range(4):
#                 dx, dy = moves[i]
#                 x_new, y_new = x+dx, y+dy
#                 if not (0 <= x_new < m and 0 <= y_new < n):
#                     continue
                
#                 if grid[x][y] == i+1:
#                     if (x_new,y_new) not in distances or distances[(x_new,y_new)] > dist:
#                         heapq.heappush(hp, (dist, x_new, y_new))
#                         distances[(x_new, y_new)] = dist
#                 else:
#                     if (x_new,y_new) not in distances or distances[(x_new,y_new)] > dist+1:
#                         heapq.heappush(hp, (dist+1, x_new, y_new))
#                         distances[(x_new, y_new)] = dist+1
