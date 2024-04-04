class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
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
