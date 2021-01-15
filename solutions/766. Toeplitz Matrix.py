class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ### Soln 2 - LeetCode solution, very clever, compare with top-left neighbor
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
           for r, row in enumerate(matrix)
           for c, val in enumerate(row))
​
#         ### Soln 1 - explicity writing out all indices
#         m = len(matrix)
#         n = len(matrix[0])
        
#         for j in range(0, n):
#             for i in range(1, min(m,n-j)):
#                 if matrix[0][j] != matrix[i][i+j]:
#                     return False
                
#         for i in range(1,m):
#             for j in range(1,min(m-i,n)):
#                 if matrix[i][0] != matrix[i+j][j]:
#                     return False
                
#         return True
