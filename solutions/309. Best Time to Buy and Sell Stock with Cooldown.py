class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # #LeetCode state machine
        # #Time O(N), space O(1)
        # sold, held, reset = float('-inf'), float('-inf'), 0
        # for i in range(len(prices)):
        #     sold, held, reset = held+prices[i], max(held, reset-prices[i]), max(reset, sold)
        # return max(sold, reset)
        
        #LeetCode DP, time O(N^2), space O(N)
        n = len(prices)
        dp = [0]*(n+2)
        
        for i in range(n-1, -1, -1):
            buyNsell = 0 # Case 1). buy and sell the stock
            for sell in range(i+1, n):
                profit = (prices[sell] - prices[i]) + dp[sell+2]
                buyNsell = max(profit, buyNsell)
                
            notBuy = dp[i+1] # Case 2). do no transaction with the stock prices[i]
            dp[i] = max(buyNsell, notBuy)
        return dp[0]
