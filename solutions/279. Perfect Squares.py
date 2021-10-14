#from collections import deque
class Solution:
    def numSquares(self, n: int, dp = {1:1}) -> int:
        # soln 4 - Jake's recursive soln
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        ans = n #0
        for sq in square_nums:
            if n-sq not in dp:
                dp[n-sq] = self.numSquares(n-sq, dp)
            ans = min(ans, dp[n-sq]+1)
        return ans
        
        # soln 3 - Leetcode recursive
        #square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        #dp = [float('inf')] * (n+1)
        #bottom case
        #dp[0] = 0
        #for i in range(1, n+1):
        #    for square in square_nums:
        #        if i < square:
        #            break
        #        dp[i] = min(dp[i], dp[i-square]+1)
        #return dp[-1]
        
        # soln 2 - Leetcode Brute-force Enumeration (Time Limit Exceeded)
        #square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        
        #def minNumSquares(k):
            #bottom cases: find a square number
        #    if k in square_nums:
        #        return 1
        #    min_num = float('inf')
            
