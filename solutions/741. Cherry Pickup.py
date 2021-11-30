class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:    
        #soln 1 - Leetcode DP w memoization, time O(N^3) due to all possible states in dp, space O(N^3)
        n = len(grid)
        memo = [[[None] * n for _1 in range(n)] for _2 in range(n)]
        
        def dp(r1, c1, c2):
            r2 = r1+c1-c2 #after t steps, r1+c1 = t = r2+c2
            if r1==n or c1==n or c2==n or r2==n or grid[r1][c1]==-1 or grid[r2][c2]==-1:
                return float('-inf') 
            elif r1==n-1 and c1==n-1:
                return grid[-1][-1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] if c1==c2 else grid[r1][c1]+grid[r2][c2]
                ans += max(dp(r1+1,c1,c2), dp(r1,c1+1,c2), dp(r1+1,c1,c2+1), dp(r1,c1+1,c2+1))
                memo[r1][c1][c2] = ans
                return ans
        #if dfs(0,0,0) return float('-inf'), then there is no viable path
        return max(0, dp(0,0,0))
    
#         #soln 2 - Leetcode greedy, WRONG solution, Time O(N^2), Space O(N^2)
#         #counterexample [[1,1,1,0,0],[0,0,1,0,1],[1,0,1,0,0],[0,0,1,0,0],[0,0,1,1,1]], return 10, truth - 11
#         def bestpath(grid):
#             N = len(grid)
#             NINF = float('-inf')
#             dp = [[NINF] * N for _ in range(N)]
#             dp[-1][-1] = grid[-1][-1]
#             for i in range(N-1, -1, -1):
#                 for j in range(N-1, -1, -1):
#                     if grid[i][j] >= 0 and (i != N-1 or j != N-1):
#                         dp[i][j] = max(dp[i+1][j] if i+1 < N else NINF,
#                                        dp[i][j+1] if j+1 < N else NINF)
#                         dp[i][j] += grid[i][j]
​
#             if dp[0][0] < 0: return None
#             ans = [(0, 0)]
#             i = j = 0
#             while i != N-1 or j != N-1:
#                 if j+1 == N or i+1 < N and dp[i+1][j] >= dp[i][j+1]:
#                     i += 1
#                 else:
#                     j += 1
#                 ans.append((i, j))
#             return ans
#         ans = 0
#         path = bestpath(grid)
#         if path is None: return 0
​
#         for i, j in path:
#             ans += grid[i][j]
#             grid[i][j] = 0
            
#         for i, j in bestpath(grid):
#             ans += grid[i][j]
​
#         return ans
