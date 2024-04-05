class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#         #soln 1 - Leetcode bit manupulation, Time O(N^2), space O(1)
#             N = 9
#             rows = [0] * N
#             cols = [0] * N
#             boxes = [0] * N
            
#             for r in range(N):
#                 for c in range(N):
#                     if board[r][c] == ".":
#                         continue
#                     pos = int(board[r][c]) - 1
#                     pos_bit = 1 << pos
                    
#                     if rows[r] & pos_bit:
#                         return False
#                     rows[r] |= pos_bit
                    
#                     if cols[c] & pos_bit:
#                         return False
#                     cols[c] |= pos_bit
                    
#                     idx = (r//3) * 3 + c//3
#                     if boxes[idx] & pos_bit:
#                         return False
#                     boxes[idx] |= (1 << pos)
#             return True
            
#         #soln 2 - use array of fixed length, Time O(N^2), space O(N^2)
        N = 9
        rows = [[0]*N for _ in range(N)]
        cols = [[0]*N for _ in range(N)]
        boxes = [[0]*N for _ in range(N)]
        
        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue
                pos = int(board[r][c]) - 1
                
                if rows[r][pos]:
                    return False
                rows[r][pos] = 1
                
                if cols[c][pos]:
                    return False
                cols[c][pos] = 1
                
                idx = (r//3) * 3 + c//3
                if boxes[idx][pos]:
                    return False
                boxes[idx][pos] = 1
        return True
​
