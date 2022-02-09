class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #Same state machine idea, but easier than 309. Best Time to Buy and Sell Stock with Cooldown
        #time O(N), space O(1)
        sold, held = 0, float('-inf')
        for i in range(len(prices)):
            sold, held = max(sold, held+prices[i]-fee), max(held, sold-prices[i])
        return max(sold, held)
        
        #Time O(N^2), space O(N), LTE
#         n = len(prices)
#         dp = [0] * (n+1)
        
#         for i in range(n-1,-1,-1):
#             # Case 1). buy and sell the stock
#             buyNsell = 0
#             for sell in range(i+1,n):
#                 profit = prices[sell]-prices[i]-fee + dp[sell+1]
#                 buyNsell = max(buyNsell, profit)
            
#             # Case 2). do no transaction with the stock prices[i]
#             notBuy = dp[i+1]
#             # print(i, buyNsell, notBuy, max(buyNsell, notBuy))
#             dp[i] = max(buyNsell, notBuy)
#         # print(dp)
#         return dp[0]
