class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ##soln1 - Leetcode more logical, first transpose, then reflect
        n = len(matrix)
        def transpose(M):
            for i in range(n):
                for j in range(i+1,n):
                    M[i][j], M[j][i] = M[j][i], M[i][j]
                    
        def reflect(M):
            for i in range(n):
                for j in range(n//2):
                    M[i][j], M[i][n-1-j] = M[i][n-1-j], M[i][j]
                    
        transpose(matrix)
        reflect(matrix)        
        
        # ##soln 0 - Leetcode, standard entry-by-entry rotation
        # n = len(matrix)
        # for i in range(n//2+n%2):
        #     for j in range(n//2):
        #         tmp = matrix[n-1-j][i]
        #         matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
        #         matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
        #         matrix[j][n-1-i] = matrix[i][j]
        #         matrix[i][j] = tmp
        
        # #Old attempt
        # for i in range(len(matrix)//2):
        #     matrix[i], matrix[~i] = matrix[~i], matrix[i]
        # matrix[:] = list(map(list,zip(*matrix)))
​
​
