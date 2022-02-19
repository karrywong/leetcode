class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #Alternative bottom-up recursion with memo, inspired by calvinchankf's soln
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        def dfs(i, j):
            if (i,j) in seen:
                return seen[(i,j)]
            if i == m-1 and j == n-1:
                return 1
            elif i > m-1 or j > n-1:
                return 0
            if obstacleGrid[i][j]:
                seen[(i,j)] = 0
                return 0
            down = dfs(i+1, j)
            right = dfs(i, j+1)
            seen[(i,j)] = down + right
            return seen[(i,j)]
        
        seen = {}
        return dfs(0,0)
        
#         #First attempt using DP, time O(MN), space O(1)
#         if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
#             return 0
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         for i in range(m):
#             for j in range(n):
#                 if obstacleGrid[i][j] == 1:
#                     obstacleGrid[i][j] = -1
#         for i in range(m):
#             for j in range(n):
#                 if obstacleGrid[i][j] == -1:
#                     continue
                    
#                 if i == 0 and j == 0:
#                     obstacleGrid[i][j] = 1
#                 elif i == 0:
#                     obstacleGrid[i][j] = obstacleGrid[i][j-1] if obstacleGrid[i][j-1] != -1 else 0
#                 elif j == 0:
#                     obstacleGrid[i][j] = obstacleGrid[i-1][j] if obstacleGrid[i-1][j] != -1 else 0
#                 else:
#                     if obstacleGrid[i][j-1] != -1:
#                         obstacleGrid[i][j] += obstacleGrid[i][j-1]
#                     if obstacleGrid[i-1][j] != -1:
#                         obstacleGrid[i][j] += obstacleGrid[i-1][j]
#         return obstacleGrid[-1][-1]
