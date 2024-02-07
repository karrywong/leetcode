class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #TBRV
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            dirs = {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}
            for x, y in dirs:
                if 0 <= x < n and 0 <= y < m:
                    if matrix[x][y] > matrix[i][j]:
                        dp[i][j] = max(dp[i][j], dfs(x, y))
            dp[i][j] += 1
            return dp[i][j]
        
        if not matrix or not matrix[0]:
            return 0
        res = 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))
        return res
