class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #Time O(M+N), space O(1)
        def binary_search_row(l, r, vec):
            while l < r:
                mid = ((l+r) >> 1)
                if vec[mid] < target:
                    l = mid + 1
                elif vec[mid] > target:
                    r = mid
                else:
                    return mid
            return l
        
        def binary_search_col(l, r, vec):
            while l < r:
                mid = ((l+r) >> 1) + 1
                if vec[mid] < target:
                    l = mid
                elif vec[mid] > target:
                    r = mid - 1  
                else:
                    return mid
            return l   
        
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                vec = matrix[i][j:]
                dj = binary_search_row(0, len(vec)-1, vec)
                if dj == 0:
                    break
                j += dj
            else: # matrix[i][j] > target
                vec = [matrix[k][j] for k in range(i)]
                di = binary_search_col(0, i-1, vec)
                if i == di:
                    break
                i = di
        return False
    
#         ###Soln 1 - Leetcode search space reduction, Time O(N+M)
#         if matrix[0][0] > target or matrix[-1][-1] < target: 
#             return False
#         rows = len(matrix)
#         columns = len(matrix[0])
#         row = 0
#         column = columns - 1
#         while(row < rows and column >= 0):
#             if matrix[row][column] == target:
#                 return True
            
#             if matrix[row][column] > target:
#                 column -= 1
#             if matrix[row][column] < target:
#                 row += 1
#         return False
