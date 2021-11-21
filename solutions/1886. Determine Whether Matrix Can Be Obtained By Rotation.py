class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        #Check all four rotations of mat
        n = len(mat)
        def transpose(M):
            for i in range(n):
                for j in range(i+1,n):
                    M[i][j], M[j][i] = M[j][i], M[i][j]
                    
        def reflectlr(M):
            for i in range(n):
                for j in range(n//2):
                    M[i][j], M[i][~j] = M[i][~j], M[i][j]
        
        if mat == target: return True
        for _ in range(3):
            transpose(mat)
            reflectlr(mat)
            if mat == target: return True
        return False
