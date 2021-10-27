class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #soln 1 - second attempt, pointers
        profit = 0
        i = 0 #i:buy day
        for j in range(1, len(prices)): #sell day
            if prices[j] < prices[i]:
                i = j
            else:
                profit = max(profit, prices[j]-prices[i])
        return profit
        
        # #soln 0 - first attempt, Time O(N)
        # minval = prices[0]
        # ans = 0
        # for p in prices:
        #     if p > minval:
        #         ans = max(ans,p - minval)
        #     else:
        #         minval = p
        # return ans
