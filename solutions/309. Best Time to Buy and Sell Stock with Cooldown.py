class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ### Soln 0 - completely failed...
        ### Soln 1 - LeetCode solution, really smart - state machine focused on "sold", "held", "reset"
        #create list of profits
        sold, held, reset = float('-inf'), float('-inf'), 0
​
        for price in prices:
            # Alternative: the calculation is done in parallel.
            # Therefore no need to keep temporary variables
            #sold, held, reset = held + price, max(held, reset-price), max(reset, sold)
​
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)
​
        return max(sold, reset)
        
            
        
