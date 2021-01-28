class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ### Soln - failed attempt, not even tried, jump directly into LeetCode solution
        ## step 1. initialize condiditions for backtracking
        rows, cols = len(grid), len(grid[0])
​
        # initial and final states
        non_obstacles = 0
        start_row, start_col = 0,0 
        for i in range(0, rows):
            for j in range(0, cols):
                cell = grid[i][j]
                if cell >= 0:
                    non_obstacles += 1
                if cell == 1:
                    start_row, start_col = i, j
                    
        path_count = 0 #initialize path count
        
        # step 2. backtrack on the grid 
        def backtrack(i, j, remain):
            nonlocal path_count
            
            #base for the termination of backtracking
            if grid[i][j] == 2 and remain == 1:
                path_count += 1 #reach destination via a valid path
                return
​
            #Mark square as visited
            temp = grid[i][j]
            grid[i][j] = -2
            remain -= 1
            
            #explore the 4 potential directions around
            for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = i + ro, j + co
