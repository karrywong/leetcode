class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         #Leetcode DP - recursive top down w memoization
#         #Time O(amount*len(coins)), space O(amount)
#         if amount < 1: return 0
#         self.count = [0]*(amount+1)
        
#         def helper(coins, rem):
#             if rem < 0: return -1
#             if rem == 0: return 0
#             if self.count[rem]: return self.count[rem]
​
#             mval = float('inf')
#             for c in coins:
#                 res = helper(coins, rem-c);
#                 if res >= 0 and res < mval:
#                     mval = 1 + res
#             self.count[rem] = -1 if mval == float('inf') else mval
#             return self.count[rem]
    
#         ans = helper(coins, amount)
#         return ans
        
        # my solution - replicate of soln for prob #279 Perfect Squares
        #Time O(amount*len(coins)), space O(amount)
        coins.sort()
        dp = [float('inf')]*(amount+1)
        #bottom case:
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i < c: break
                dp[i] = min(dp[i], dp[i-c]+1)
        return dp[-1] if dp[-1] != float('inf') else -1
