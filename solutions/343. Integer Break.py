class Solution:
    def integerBreak(self, n: int) -> int:
        # one-liner in time O(1) from cjporteo
        #<https://leetcode.com/problems/integer-break/discuss/285876/Python-O(1)-one-line-solution-detailed-explanation>
        # return int(math.pow(2, (-n)%3) * math.pow(3, (n-1)%3 + (n-4)//3)) if n > 3 else n-1
​
        #First attempt, followed hints 1 and 2, time O(N)
        dp = [0,1,1,2,4,6,9]
        if n <= 6: return dp[n]
        dp = dp + [0]*(n-6)
        for i in range(7,n+1):
            dp[i] = 3*dp[i-3]
            # for j in range(1,4):
                # dp[i] = max(dp[i], dp[i-j]*j)
        return dp[-1]
