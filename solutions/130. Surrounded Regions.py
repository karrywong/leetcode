class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #First attempt, soln 0 - slow, time O(MN)
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        def getNeighbor(r,c):
            for move in moves:
                yield r+move[0], c+move[1]
                
        m, n = len(board), len(board[0])
        seen = set()
        for r0 in range(1,m-1):
            for c0 in range(1,n-1):
                if (r0, c0) in seen:
                    continue
                if board[r0][c0] == "O":
                    stack = [(r0,c0)]
                    seen.add((r0,c0))
                    bo, captured = True, set([(r0,c0)])
​
                    while stack:
                        r,c = stack.pop()
                        for x,y in getNeighbor(r,c):
                            if 1<=x<m-1 and 1<=y<n-1 and board[x][y] == "O" and (x,y) not in seen:
                                stack.append((x,y))
                                seen.add((x,y))
                                captured.add((x,y))
                            elif (x==0 or x==m-1 or y==0 or y==n-1) and board[x][y] == "O":
                                bo = False
                    
                    if bo: #make sure that the whole region is captured
                        for x,y in captured:
                            board[x][y] = "X"
