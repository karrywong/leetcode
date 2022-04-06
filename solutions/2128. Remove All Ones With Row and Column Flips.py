class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        #Tricky, soln by idontknoooo
        #time O(M*N), space O(N), where M, N = len(grid), len(grid[0])
        r0, r0_invert = grid[0], [1-val for val in grid[0]]
        for i in range(1, len(grid)):
            if grid[i] != r0 and grid[i] != r0_invert:
                return False
        return True        
    
        # #One-liner
        # return all(grid[i] == grid[0] or grid[i] == [1-val for val in grid[0]] for i in range(1,len(grid)))
​
            
