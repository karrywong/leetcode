from collections import deque
​
​
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #Optimized with overwrite, BFS, Time O(N^2), Space O(N^2)
        #similar but easier than 752. Open the Lock
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        def _find_next_step(x:int, y:int, step:int, n:int) -> None:
            for dx, dy in directions:
                x_new, y_new = x+dx, y+dy
                if 0<=x_new<n and 0<=y_new<n and grid[x_new][y_new] == 0 and (x_new,y_new) not in seen:
                    queue.append((x_new, y_new, step+1))
                    seen.add((x_new, y_new))
            return
        
        upper_bound = n*n+1
        ans = upper_bound
        queue = deque([(0,0,1)])
        seen = set([(0,0)]) 
        while queue:
            x, y, step = queue.popleft()
            if x == n-1 and y == n-1:
                ans = min(ans, step)
                continue
            _find_next_step(x,y,step,n)
        return ans if ans < upper_bound else -1
​
#         # DFS, time O(N), space O(N)
#         if grid[0][0]==1: return -1
#         n = len(grid)
#         moves = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
#         max_int = 10**4+1
        
#         def helper(x, y, cnt) -> int:
#             if x == n-1 and y == n-1:
#                 return cnt
​
#             if x<0 or x>=n or y<0 or y>=n or grid[x][y] != 0:
#                 return max_int
            
#             grid[x][y] = 2
#             cost = max_int
#             for dx, dy in moves:
#                 next_cnt = helper(x+dx, y+dy,cnt+1)
#                 cost = min(cost, next_cnt)
#             grid[x][y] = 0
            
#             return cost
        
#         ans = helper(0,0,1)
#         return -1 if ans == max_int else ans
