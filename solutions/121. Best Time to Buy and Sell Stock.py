class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0 # i - buy day
        j = 1 # j - sell day
​
        for j in range(1, len(prices)):
            if prices[i] > prices[j]:
                i = j
            
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
        return profit
​
            
        
