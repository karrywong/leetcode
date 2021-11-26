class Solution:
    def __init__(self):
        self.lib = {}
    def uniquePaths(self, m: int, n: int) -> int:
        #third attempt, recursion w memoization, slow
        if m == 1 or n == 1:
            return 1
        if (m,n) in self.lib:
            return self.lib[(m,n)]
        
        temp = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        self.lib[(m,n)] = temp
        self.lib[(n,m)] = temp
        return temp
        
        #second attempt - nCk, Time less than O((M+N)^2), Space O(1)
        # return math.comb(m+n-2, m-1) 
        # return math.factorial(m + n - 2) // math.factorial(n - 1) // math.factorial(m - 1)
        
        # #First attempt - dynamic programming, Time O(M*N), Space O(min(M,N))
        # if m < n: #ensure n <= m
        #     m, n = n, m
        # dp = [1]*n
        # for _ in range(1, m):
        #     for j in range(1, n):
        #         dp[j] += dp[j-1]
        # return dp[-1]
