class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:        
        ### Soln 1 - Karry & Jake
        ### idea: go down first column and enumerate along the last list:
        # 0 <= i <= m, 0 <= j <= n
        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        
        for i in range(0, m):
            temp = []
            for k in range(0,min(i+1,n)):
                temp.append(matrix[i-k][k])
            if i % 2 == 1: temp.reverse()
            res.extend(temp)
​
        for j in range(1,n):
            temp = []
            for k in range(j, min(m+j,n)):
                temp.append(matrix[m+j-k-1][k])
            if (m-1+j) % 2 == 1: temp.reverse()
            res.extend(temp)
        
        return res
    
 
