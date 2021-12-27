class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # #Stefan Pochmann's two liner
        # cols = [[(j, b) for j, b in enumerate(col) if b] for col in zip(*mat2)]
        # return [[sum(row[j]*b for j, b in col) for col in cols] for row in mat1]
        
        #Inspired by Stefan Pochmann, Time O(N^3) but using sparsity
        cols = []
        for i, col in enumerate(zip(*mat2)):
            cols.append([])
            for j, b in enumerate(col):
                if b:
                    cols[i].append((j,b))
        
        ans = []
        for i, row in enumerate(mat1):
            ans.append([])
            for col in cols:
                ans[i].append(sum(row[j]*b for j, b in col))
        return ans        
        
#         #Standard, Time O(N^3), no use of sparsity
#         m, n = len(mat1), len(mat1[0])
#         p = len(mat2[0])
#         ans = [[0] * p for _ in range(m)]
        
#         for i in range(n):
#             for j in range(m):
#                 for k in range(p):
#                     ans[j][k] += mat1[j][i]*mat2[i][k]
#         return ans        
