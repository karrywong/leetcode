class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # p1 + p2 + ... + pn = k 
        #  C(k+n-1, n-1)
        # (p1 + 1) + (p2 + 1) + ... + (pn + 1) = k + n
        
        #Too hard, need to consult soln by lee215
        #Time O(N*M), space O(N*k), where N = len(piles), M = sum(piles[i].length)
        dp = [[None] * (k+1) for _ in range(len(piles)+1)]
        def helper(i, k): #dynamic programming, i-th pile,
            if dp[i][k]:
                return dp[i][k]
            
            if k == 0 or i == len(piles): 
                return 0
            
            res, cur = helper(i + 1, k), 0
            for j in range(min(len(piles[i]), k)):
                cur += piles[i][j]
                res = max(res, cur + helper(i+1, k-j-1))
            dp[i][k] = res
            return res
        return helper(0,k)
