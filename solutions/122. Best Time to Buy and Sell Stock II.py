class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #One-liner
        return sum([prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] - prices[i-1] > 0])
        
        # #First attempt, solved in 5 min
        # #Time: O(N), Space: O(1)
        # ans = 0
        # for i in range(1, len(prices)):
        #     change = prices[i] - prices[i-1]
        #     if change > 0:
        #         ans += change
        # return ans
