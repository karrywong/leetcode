class Solution:    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ###Soln 1
#         if target < matrix[0][0] or target > matrix[-1][-1]: return False
        
#         i = 0 
#         while i < len(matrix):
#             if target >= matrix[i][0] and target <= matrix[i][-1]:
#                 if target in matrix[i]: return True
#             i += 1
#         return False
    
        ###Soln 3
        # entire = [x for l in matrix for x in l]
        # if target in entire:
        #     return True
        # else: 
        #     return False
        
        ###Soln 4 - two pointers
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        row = 0
        column = columns - 1
        while(row < rows and column >= 0):
            if matrix[row][column] == target:
                return True
            
            if matrix[row][column] > target:
                column -= 1
            if matrix[row][column] < target:
                row += 1
        return False
