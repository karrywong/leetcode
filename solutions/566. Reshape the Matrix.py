class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        #First attempt, Time O(m*n), Space O(m*n)
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        else:
            lst = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(m):
            for j in range(n):
                x, y = divmod(i*n + j, c)
                lst[x][y] = mat[i][j]
        return lst
