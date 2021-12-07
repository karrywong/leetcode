class Solution:
    #helper func to compute max gain and return correpsonding left and right indices
    #time: O(N), space O(1)
    def helper(self, lst):
        if not lst: return 0,0,0
        gain, buy_day = 0, lst[0]
        temp, left, right = 0, 0, 0
        for i in range(1, len(lst)):
            if lst[i] <= buy_day:
                buy_day = lst[i]
                temp = i 
            else: #prices[i] >= buy_day
                val = lst[i] - buy_day
                if gain < val:
                    gain = val
                    right = i
                    left = temp
        return gain, left, right
    
    def maxProfit(self, prices: List[int]) -> int:
        ### Cho's idea - First, get left and right indices for array with max gain,ie [0,...,4]
        ### Second, case I - no overlap with another max gain, done
        ### Third, case II - with overlap, just find the max two gains within [0,..,4]
        #Time: O(N), Space O(1)
        
        #First, get l1 and r1 where prices[r1] - prices[l1] is the max gain in prices
        ans0, l1, r1 = self.helper(prices)
        #case I
        left_max, _, _ = self.helper(prices[:l1+1])
        right_max, _, _ = self.helper(prices[r1+1:])
        ans1 = ans0 + max(left_max, right_max) 
        #case II
        _, l2, r2 = self.helper(prices[l1:r1+1][::-1]) #reverse array to find the break 
        l2, r2 = (r1-l1)-r2, (r1-l1)-l2  #since the array is reversed, not obvious
        ans2 = (prices[l2+l1] - prices[l1]) + (prices[r1] - prices[l1+r2])
        return max(ans1, ans2)
