class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
#         ###Bonus - Stefan Pochmann's soln for sparse matrix
#         def gameOfLifeInfinite(self, live: set) -> set:
#             ctr = collections.Counter((I, J) for i, j in live for I in range(i-1, i+2) for J in range(j-1, j+2) \
#                                       if I != i or J != j)
#             return {ij for ij in ctr if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}
        
#         def gameOfLife(self, board):
#             live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
#             live = self.gameOfLifeInfinite(live)
#             for i, row in enumerate(board):
#                 for j in range(len(row)):
#                     row[j] = int((i, j) in live)        
        
        #Soln 2 - Use tricks -1: live->dead and 2: dead->live, time O(M*N), space O(1)
        moves = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                live_ngh = 0
                for di, dj in moves:
                    i_new, j_new = i+di, j+dj
                    if 0 <= i_new < m and 0 <= j_new < n and abs(board[i_new][j_new])==1:
                        live_ngh += 1
               
                if board[i][j] == 1 and (live_ngh < 2 or live_ngh > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and live_ngh == 3:
                    board[i][j] = 2 
        # print(board)   
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0
        
#         #Soln 1 - Straightforward simulation, time O(M*N) but space O(M*N)
#         moves = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
#         m, n = len(board), len(board[0])
#         board_copy = [[board[i][j] for j in range(n)] for i in range(m)]
        
#         for i in range(m):
#             for j in range(n):
#                 live_ngh = 0
#                 for di, dj in moves:
#                     i_new, j_new = i+di, j+dj
#                     if 0 <= i_new < m and 0 <= j_new < n and board_copy[i_new][j_new]:
#                         live_ngh += 1
               
#                 if board_copy[i][j]:
#                     if live_ngh < 2 or live_ngh > 3:
#                         board[i][j] = 0
#                 else:
#                     if live_ngh == 3:
#                         board[i][j] = 1
