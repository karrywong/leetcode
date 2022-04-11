class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for _ in range(m)]
        total = m*n
        for i in range(m):
            for j in range(n):
                j_new = j+k
                if j_new >= n:
                    di, j_new = divmod(j_new, n)
                    i_new = i+di
                    ans[i_new if i_new < m else i_new % m][j_new] = grid[i][j]
                else:
                    ans[i][j_new] = grid[i][j]
        return ans
                
            
