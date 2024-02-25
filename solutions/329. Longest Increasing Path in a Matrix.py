from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #TBRV, time O(M*N), space O(M*N)
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            dirs = {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}
            for x, y in dirs:
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                        dp[i][j] = max(dp[i][j], dfs(x, y))
            dp[i][j] += 1
            return dp[i][j]
        
        res = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        print(dp)
        return res
    
# 1 2 3
# 8 9 4
# 7 6 5
​
#dp 
# 9 8 7
# 2 1 6
# 3 4 5
​
#         # faster solution, time O(M*N*log(M*N)), space O(M*N)
#         m = len(matrix)
#         if m == 0:
#             return 0
#         n = len(matrix[0])
#         record = [[0 for _ in range(n)] for _ in range(m)]
​
#         # pre-processing
#         lookup = defaultdict(list) # key: integer in grid, value: list of its coordinates (i,j)
#         for i in range(m):
#             for j in range(n):
#                 lookup[matrix[i][j]].append((i,j))   
​
#         dxy = [(0,1), (-1,0), (0,-1), (1,0)]
#         # sort all integers seen
#         for num in sorted(lookup.keys()):
#             for i, j in lookup[num]:
#                 res = 1
#                 for dx, dy in dxy:
#                     h, k = i+dx, j+dy
#                     if h < 0 or h >= m or k < 0 or k >= n:
#                         continue
#                     if num > matrix[h][k]:
#                         res = max(res, record[h][k]+1)
#                 record[i][j] = res
​
#         return max(max(row) for row in record)        
