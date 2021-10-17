class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        # leetcode - recursive top down
        if amount < 1: return 0
        count = [0]*(amount+1)
        
        def helper(coins, rem, count):
            if rem < 0: return -1
            if rem == 0: return 0
            if count[rem]: return count[rem]
​
            mval = float('inf')
            for c in coins:
                res = helper(coins, rem-c, count);
                if res >= 0 and res < mval:
                    mval = 1 + res
            count[rem] = -1 if mval == float('inf') else mval
            return count[rem]
        
        ans = helper(coins, amount, count)
        #print(count)
        return ans
        
        
        
        # my solution - replicate of soln for prob #279 Perfect Squares
        coins.sort()
        dp = [float('inf')]*(amount+1)
        #bottom case:
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
