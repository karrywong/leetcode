class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #DP soln, time O(len(costs)), space O(1)
        dp = costs[0]
        for i in range(1, len(costs)):
            dp[0], dp[1], dp[2] = costs[i][0] + min(dp[1], dp[2]), costs[i][1] + min(dp[0], dp[2]), costs[i][2] + min(dp[0], dp[1])
        return min(dp)
​
