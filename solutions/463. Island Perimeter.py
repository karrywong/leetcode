class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #soln 1 - Leetcode, better count:
        ans = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val:
                    ans += 4
                
                    if r > 0 and grid[r-1][c]:
                        ans -= 2
                    if c > 0 and grid[r][c-1]:
                        ans -= 2
        return ans
                        
        #soln 0 - first attempt, time O(MN)
#         m, n = len(grid), len(grid[0])
#         ans = 0
#         for r, row in enumerate(grid):
#             for c, val in enumerate(row):
#                 if val:
#                     if r == 0:
#                         ans += 1
#                     else: #r > 0
#                         if grid[r-1][c] == 0: 
#                             ans += 1
                    
#                     if r == m-1:
#                         ans += 1
#                     else: #r < m-1
#                         if grid[r+1][c] == 0:
#                             ans += 1
                    
