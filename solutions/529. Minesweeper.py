class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
#         # DFS time O(M*N), space O(M*N)
#         m, n = len(board), len(board[0])
#         x,y = click
#         if board[x][y] == "M":
#             board[x][y] = "X"
#             return board
        
#         dxy = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
#         def dfs(i:int, j:int) -> None:
#             if board[i][j] == "E":
#                 nghs = [(i+dx, j+dy) for dx,dy in dxy if 0<=i+dx<m and 0<=j+dy<n]
#                 cnt_mine = sum([board[i_next][j_next] == "M" for i_next, j_next in nghs])
#                 if cnt_mine > 0:
#                     board[i][j] = str(cnt_mine)
#                 else:
#                     board[i][j] = "B"
#                     for i_next, j_next in nghs:
#                         dfs(i_next, j_next)
#             return
#         dfs(x,y)
#         return board
        
        
        # BFS time O(M*N), space O(M*N)
        m, n = len(board), len(board[0])
        x,y = click
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        
        queue = collections.deque([tuple(click)])
        seen = set(tuple(click))
        dxy = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
        
        while queue:
            for _ in range(len(queue)):
                x0,y0 = queue.popleft()
                ngh = []
                cnt_mine = 0
                for dx, dy in dxy:
                    x1, y1 = x0+dx, y0+dy
                    if 0 <= x1 < m and 0 <= y1 < n:
                        if board[x1][y1] == "M":
                            cnt_mine += 1
                        elif (x1,y1) not in seen and board[x1][y1] == "E":
                            ngh.append((x1,y1))
​
                if cnt_mine > 0:
                    board[x0][y0] = str(cnt_mine)
                else:
                    board[x0][y0] = "B"
                    queue.extend(ngh)
                    seen.update(ngh)
        return board        
