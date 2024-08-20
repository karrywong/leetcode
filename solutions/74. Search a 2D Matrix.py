class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        ###Soln 2 - Leetcode, time O(log(MN))
        m, n = len(matrix),len(matrix[0])
        # binary search
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r-l) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if target == val:
                return True
            elif target < val:
                r = mid - 1
            else:
                l = mid + 1
        return False
        
#         #soln 0 - Time O(M*log(N)) where matrix is MxN
#         m, n = len(matrix),len(matrix[0])
#         for row in range(m):
#             if target > matrix[row][-1]:
#                 continue
#             if target < matrix[row][0]:
#                 break
            
#             l, r = 0, n-1
#             while l <= r:
#                 mid = l + (r-l)//2
#                 if matrix[row][mid] == target:
#                     return True
#                 elif matrix[row][mid] < target:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return False
