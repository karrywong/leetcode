class Solution:
    def numTrees(self, n: int) -> int:
        #LeetCode - deduce recursive formula for Catalan number from BST
        #Time O(N^2), space O(N)
        dp = [1]*2 + [0]*(n-1)
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]
        
        # #First attempt, compute Catalan number, time O(N), space O(1)
        # @lru_cache(maxsize = None)
        # def catalan(n):
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     return int(2*(2*n-1)/(n+1) * catalan(n-1))
        # return catalan(n)
