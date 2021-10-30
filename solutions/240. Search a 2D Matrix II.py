class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ###Soln 1 - Leetcode search space reduction, Time O(N+M)
        if matrix[0][0] > target or matrix[-1][-1] < target: 
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
        
        # soln 0 - first attempt, Time O(log(n!)), Space O(1)
        # if matrix[0][0] > target or matrix[-1][-1] < target: 
        #     return False
        # m, n = len(matrix), len(matrix[0])
        # if m == n: 
        #     i, j = 0, 0
        # elif m < n:
        #     i, j = 0, n-m
        # else:
        #     i, j = m-n, 0
        # while i < m and j < n:
        #     if matrix[i][j] < target:
        #         i += 1
        #         j += 1
