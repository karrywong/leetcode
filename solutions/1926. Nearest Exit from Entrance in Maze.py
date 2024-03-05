from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Should ask at the beginning if I can modify maze
        # "+","+", 1 ,"+"
        #  2,  1,  0,"+"
        # "+","+","+", 
        
        # "+","+","+"
        #  0,  1,  2
        # "+","+","+"
        
        # 0,"+" -> -1
        
        ans = -1        
        rows = len(maze)
        if rows == 0: 
            return ans
        cols = len(maze[0])
        x0, y0 = entrance
        maze[x0][y0] = "+"
        dq = deque([(x0, y0, 0)])
        
        while dq:
            x, y, cnt = dq.popleft()
            cnt += 1
            for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                x_next, y_next = x+dx, y+dy
                if  0<= x_next < rows and 0 <= y_next < cols and maze[x_next][y_next] == ".":
                    if x_next in (0, rows-1) or y_next in (0, cols-1):
                        return cnt
                    maze[x_next][y_next] = "+"
                    dq.append((x_next, y_next, cnt))
                    
        return ans
​
        # DFS solution, wrong direction
#         lookup = {} #key:(x,y), value: # step of shortest path to exit
#         rows, cols = len(maze), len(maze[0]) # 3,3
​
#         dxy = [(0,1), (1,0), (0,-1), (-1,0)] # ordering
#         def dfs(x:int, y:int, cnt:int=0) -> None:
#             if (x,y) in lookup:
#                 lookup[(x,y)] = min(lookup[(x,y)], cnt)
#                 return
            
#             lookup[(x,y)] = cnt
#             for dx, dy in dxy:
#                 x_next, y_next = x+dx, y+dy
#                 if 0<= x_next < rows and 0 <= y_next < cols and maze[x_next][y_next] != "+":
#                     dfs(x_next,y_next,cnt+1)
        
#         dfs(entrance[0],entrance[1]) #dfs(1,2)
#         ans = float('inf')
        
#         for col in range(cols):
#             if maze[0][col] != "+" and (0, col) in lookup and lookup[(0,col)] != 0:
#                 ans = min(ans, lookup[(0,col)]) # ans = 1
#             if rows > 1 and maze[rows-1][col] != "+" and (rows-1, col) in lookup and lookup[(rows-1,col)] != 0:
#                 ans = min(ans, lookup[(rows-1,col)])
                
#         for row in range(rows):
#             if maze[row][0] != "+" and (row, 0) in lookup and lookup[(row,0)] != 0:
#                 ans = min(ans, lookup[(row,0)]) # ans = 1
#             if cols > 1 and maze[row][cols-1] != "+" and (row, cols-1) in lookup and lookup[(row,cols-1)] != 0:
#                 ans = min(ans, lookup[(row,cols-1)])
        
#         return ans if ans != float('inf') else -1
