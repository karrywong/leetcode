class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #soln 1 - BFS (or DFS), Time O(MN), Space O(MN)
        m, n = len(board), len(board[0])
        def traverse(board, r0, c0):
            queue = collections.deque([(r0,c0)])
            while queue:
                (x,y) = queue.popleft() #BFS, changed to queue.pop() for DFS
                if board[x][y] != 'O': continue
                board[x][y] = 'E'
                if y < n-1: queue.append((x,y+1))
                if x < m-1: queue.append((x+1,y))
                if y > 0: queue.append((x,y-1))
                if x > 0: queue.append((x-1,y))
            
        boarders = list(itertools.product(range(m), [0, n-1])) + list(itertools.product([0, m-1], range(n)))
        for row, col in boarders: #mark the "escaped" cells, with any placeholder, e.g. 'E'
            traverse(board, row, col)
​
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O': board[r][c] = 'X' #captured 
                elif board[r][c] == 'E': board[r][c] = 'O' #escaped
                    
#         #First attempt, soln 0 - time O(MN), large memory used, can be up to O(M^2*N^2)!!!
#         moves = [(1,0), (0,1), (-1,0), (0,-1)]
#         def getNeighbor(r,c):
#             for move in moves:
#                 yield r+move[0], c+move[1]
                
#         m, n = len(board), len(board[0])
#         seen = set()
#         for r0 in range(1,m-1):
#             for c0 in range(1,n-1):
#                 if (r0, c0) in seen:
#                     continue
#                 if board[r0][c0] == "O":
#                     stack = [(r0,c0)]
#                     seen.add((r0,c0))
#                     bo, captured = True, set([(r0,c0)])
​
#                     while stack:
#                         r,c = stack.pop()
#                         for x,y in getNeighbor(r,c):
#                             if 1<=x<m-1 and 1<=y<n-1 and board[x][y] == "O" and (x,y) not in seen:
#                                 stack.append((x,y))
#                                 seen.add((x,y))
#                                 captured.add((x,y))
#                             elif (x==0 or x==m-1 or y==0 or y==n-1) and board[x][y] == "O":
#                                 bo = False
                    
#                     if bo: #make sure that the whole region is captured
#                         for x,y in captured:
#                             board[x][y] = "X"
