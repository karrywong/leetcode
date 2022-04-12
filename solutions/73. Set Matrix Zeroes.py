class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Leetcode's marking, space O(1) soln, time O(MN)
        m, n = len(matrix), len(matrix[0])
        is_col = False
        for i in range(m):
            # Use additional variable for 1st column and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if is_col:
            for i in range(m):
                matrix[i][0] = 0
        
#         #First attempt space O(1) soln, time O(MN)
#         m, n = len(matrix), len(matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     matrix[i][j] = None
        
#         bo = False
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] is None:
#                     bo = True
#                     break
#             if bo:
#                 for j in range(n):
#                     if matrix[i][j] is None:
#                         continue
#                     elif matrix[i][j] != 0:
#                         matrix[i][j] = 0
#             bo = False            
            
#         bo = False        
#         for j in range(n):
#             for i in range(m):
#                  if matrix[i][j] is None:
#                     bo = True
#                     break    
#             if bo:                    
#                 for i in range(m):
#                     if matrix[i][j] is None:
#                         continue
#                     elif matrix[i][j] != 0:
#                         matrix[i][j] = 0
#             bo = False            
​
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] is None:
#                     matrix[i][j] = 0
