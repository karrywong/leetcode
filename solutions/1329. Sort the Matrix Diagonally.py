class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0 for x in range(n)] for y in range(m)]
        res[-1][0], res[0][-1] = mat[-1][0], mat[0][-1]
        
        for i in range(n-1):
            temp1 = sorted([mat[k][i+k] for k in range(0,min(m,n-i))])
            for k in range(0,min(m,n-i)):
                res[k][i+k] = temp1[k]
        
        for j in range(1,m-1):
            temp2 = sorted([mat[j+k][k] for k in range(0, min(m-j,n))])
            for k in range(0, min(m-j,n)):
                res[j+k][k] = temp2[k] 
        
        return res
