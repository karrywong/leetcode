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
