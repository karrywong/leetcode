class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
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
