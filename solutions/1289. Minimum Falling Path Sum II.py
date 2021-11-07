class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        #soln 0 - DP, same as 931. Minimum Falling Path Sum
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += min(grid[i-1][1:])
            grid[i][-1] += min(grid[i-1][:n-1])
            for j in range(1, n-1):
                val1 = min(grid[i-1][:j])
                val2 = min(grid[i-1][j+1:])
                grid[i][j] = grid[i][j] + val1 if val2 > val1 else grid[i][j] + val2
        return min(grid[-1])
                    
                
        
