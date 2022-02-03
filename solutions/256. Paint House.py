class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #DP soln, time O(len(costs)), space O(1)
        dp = costs[0]
        for i in range(1, len(costs)):
            red, blue, green = dp
            dp[0] = costs[i][0] + min(blue, green)
            dp[1] = costs[i][1] + min(red, green)
            dp[2] = costs[i][2] + min(red, blue)
        return min(dp)
​
