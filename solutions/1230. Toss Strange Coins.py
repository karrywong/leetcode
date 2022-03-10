class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
#         #DP, inspired by combat_shawn
#         #Time O(len(prob) * target), space O(len(prob) * target)
#         n = len(prob)
#         dp = [[0] * (target + 1) for _ in range(n)] 
#         dp[0][0] = 1-prob[0]
        
#         if target > 0:    
#             dp[0][1] = prob[0]
            
#         for i in range(1, n):
#             dp[i][0] = dp[i-1][0]*(1-prob[i])
        
#         for i in range(1,n):
#             for j in range(1, min(n, target)+1):
#                 dp[i][j] = dp[i-1][j] * (1-prob[i]) + dp[i-1][j-1] * prob[i]
        
#         return dp[n-1][target]
    
        #DP, with space optimized, inspired by lee215
        #Time O(len(prob) * target), space O(target)
        dp = [1] + [0] * target
        for p in prob:
            for k in range(target, -1, -1):
                if k == 0:
                    dp[k] = dp[k]*(1-p)
                else:
                    dp[k] = dp[k-1]*p + dp[k]*(1-p)
        return dp[target]
