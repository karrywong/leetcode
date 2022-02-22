class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         #Problem not that hard but got stuck unfortunately and still had no clues after 10 minutes
#         #LeetCode BFS, time O(MN), space O(MN)
#         m, n = len(heights), len(heights[0])
#         pacific_queue = collections.deque([(i,0) for i in range(m)] + [(0,j) for j in range(1,n)])
#         atlantic_queue = collections.deque([(i,n-1) for i in range(m)] + [(m-1,j) for j in range(0,n-1)])
​
#         moves = [(1,0), (0,1), (-1,0), (0,-1)] #four directions
#         def bfs(queue):
#             visited = set()
#             while queue:
#                 r, c = queue.popleft()
#                 visited.add((r,c))
#                 for (dr, dc) in moves:
#                     r_new, c_new = r+dr, c+dc
#                     if 0 <= r_new < m and 0 <= c_new < n and (r_new, c_new) not in visited and heights[r_new][c_new] >= heights[r][c]:
#                         queue.append((r_new, c_new))
#             return visited
        
#         pacific_reached = bfs(pacific_queue) 
#         atlantic_reached = bfs(atlantic_queue)
#         return [[r,c] for r,c in pacific_reached.intersection(atlantic_reached)]
        
        
        #Alternative - LeetCode DFS, time O(MN), space O(MN)       
        m, n = len(heights), len(heights[0])
        pacific_reached = set()
        atlantic_reached = set()
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def dfs(r, c, visited):
            visited.add((r,c))
            for (dr, dc) in moves:
                r_new, c_new = r+dr, c+dc
                if 0 <= r_new < m and 0 <= c_new < n and (r_new, c_new) not in visited and heights[r_new][c_new] >= heights[r][c]:
                    dfs(r_new, c_new, visited)
        
        for i in range(m):
            dfs(i, 0, pacific_reached)
            dfs(i, n-1, atlantic_reached)
        for j in range(n):
            dfs(0, j, pacific_reached)
            dfs(m-1, j, atlantic_reached)
        return [[r,c] for r,c in pacific_reached.intersection(atlantic_reached)] 
