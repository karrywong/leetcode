class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #soln 0 - first attempt, DP
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            matrix[i][0] += min(matrix[i-1][0], matrix[i-1][1])
            matrix[i][-1] += min(matrix[i-1][-2], matrix[i-1][-1])
            for j in range(1, n-1):
                matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
        return min(matrix[-1])
