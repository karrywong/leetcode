class Solution:
    def integerBreak(self, n: int) -> int:
        #First attempt, followed hints 1 and 2
        dp = [0,1,1,2,4,6,9]
        if n <= 6: return dp[n]
        dp = dp + [0]*(n-6)
        for i in range(7,n+1):
            for j in range(1,4):
                dp[i] = max(dp[i], dp[i-j]*j)
        # print(dp)
        return dp[-1]
                
                            
 
        
        
