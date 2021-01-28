class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ### Soln 0 - combinatorics
        return math.comb(m + n - 2, m - 1)
    
        ### Soln 1 - Dynamic programming
        if m == 1 or n == 1: return 1
        # initialize
        res = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]
​
