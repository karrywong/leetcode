class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:        
        #Optimized with overwrite, BFS, Time O(N), Space O(N)
        #similar but easier than 752. Open the Lock
        n = len(grid)
        if grid[0][0]: return -1
        queue = collections.deque([(0,0,1)])
        grid[0][0] = 2
        # seen = set() # can be optimized
        moves = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        while queue:
            r, c, count = queue.popleft()
            if r == n-1 and c == n-1: return count
            for r0, c0 in moves:
                x,y = r+r0, c+c0
                # if 0<=x<n and 0<=y<n and grid[x][y] == 0 and (x,y) not in seen:
                    # seen.add((x,y))
                    # queue.append((x,y,count+1))
                if 0<=x<n and 0<=y<n and grid[x][y] == 0:
                    grid[x][y] = 2
                    queue.append((x,y,count+1))
        return -1
        
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
