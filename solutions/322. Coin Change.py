class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:                    
        # my solution - replicate of soln for prob #279 Perfect Squares
        coins.sort()
        dp = [float('inf')]*(amount+1)
        #bottom case:
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i < c: break
                dp[i] = min(dp[i], dp[i-c]+1)
        return dp[-1] if dp[-1] != float('inf') else -1
        
        
