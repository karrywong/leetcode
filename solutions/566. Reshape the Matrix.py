class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # #Stefan Pochmann - really short soln
        # flat = sum(mat, [])
        # if len(flat) != r * c:
        #     return mat
        # tuples = zip(*([iter(flat)] * c))
        # return map(list, tuples)
        
        #Second attempt, without divmod, Time O(m*n), Space O(m*n)
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat     
        lst = [[0 for _ in range(c)] for _ in range(r)]
        r0, c0 = 0, 0
        for i in range(m):
            for j in range(n):
                lst[r0][c0] = mat[i][j]
                c0 += 1
                if c0 == c:
                    r0 += 1
                    c0 = 0
        return lst
                
#         #First attempt, Time O(m*n), Space O(m*n)
#         m, n = len(mat), len(mat[0])
#         if m * n != r * c:
#             return mat
​
#         lst = [[0 for _ in range(c)] for _ in range(r)]
#         for i in range(m):
#             for j in range(n):
#                 x, y = divmod(i*n + j, c)
#                 lst[x][y] = mat[i][j]
#         return lst
