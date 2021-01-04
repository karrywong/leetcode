class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ### Soln 1
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        
        ### Search rows
        i = 0
        while i < len(matrix):
            if target >= matrix[i][0] and target <= matrix[i][-1]: 
                break
            i += 1
        
        if i == len(matrix): return False
        else:
            if target in matrix[i]:
                return True
            else:
                return False
            
            try:
                idx = matrix[i].index(target)
            except:
                idx = -1
        return False if idx == -1 else True
            
        #     check = [x for x in matrix[i] if x == target]
        # return True if check else False
        
        
#         ###Soln 2 - Leetcode
#         m = len(matrix)
#         if m == 0:
#             return False
#         n = len(matrix[0])
        
#         # binary search
#         left, right = 0, m * n - 1
#         while left <= right:
#                 pivot_idx = (left + right) // 2
#                 pivot_element = matrix[pivot_idx // n][pivot_idx % n]
#                 if target == pivot_element:
#                     return True
#                 else:
#                     if target < pivot_element:
#                         right = pivot_idx - 1
#                     else:
#                         left = pivot_idx + 1
#         return False
