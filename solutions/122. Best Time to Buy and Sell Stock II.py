class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            ### One pass
            answer = 0
            for i in range(1, len(prices)):
                if prices[i-1] < prices[i]:
                    answer += prices[i] - prices[i-1]
            return answer
