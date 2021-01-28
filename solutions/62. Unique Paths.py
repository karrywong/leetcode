class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ### Soln 0 - combinatorics
        return math.comb(m + n - 2, m - 1)
    
        ### Soln 1 - 
        
