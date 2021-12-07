class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #First attempt, inspired by 2nd solution for prob 123. Best Time to Buy and Sell Stock III
        cost = [float('inf')] * k 
        profit = [0]*k
        
        for price in prices:
            for i in range(k):
                cost[i] = min(cost[i], price-profit[i-1]) if i > 0 else min(cost[i], price)
                profit[i] = max(profit[i], price-cost[i])
        return profit[-1] if profit else 0
