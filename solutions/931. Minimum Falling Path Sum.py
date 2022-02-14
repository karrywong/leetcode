class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #soln 1 - 4-liner by cenkay
        #indicing [j and j - 1:j + 2] is equivalent to [((j != 0) and (j - 1)) : j+2]
        #ie, [j:j+2] if j == 0 else [j-1:j+2]
        #A and B in Python -> if not A: return A, else: return B
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] += min(matrix[i - 1][j and j - 1:j + 2])
        return min(matrix[-1])
        
        # #soln 0 - first attempt, DP, time O(N), space O(1) in-place
        # m, n = len(matrix), len(matrix[0])
        # for i in range(1, m):
        #     matrix[i][0] += min(matrix[i-1][0], matrix[i-1][1])
        #     matrix[i][-1] += min(matrix[i-1][-2], matrix[i-1][-1])
        #     for j in range(1, n-1):
        #         matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
        # return min(matrix[-1])
