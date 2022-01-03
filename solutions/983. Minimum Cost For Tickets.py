class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #Similar but trickier than 322. Coin Change
        #Totally stuck, Leetcode DP
        #time O(N), space O(N)
        n = len(days)
        durations = [1,7,30]
        
        @functools.cache
        def helper(i): #DP, helper(i) return the cost to travel from days[i] to the end of plan
            if i == n:
                return 0
            
            ans = float('inf')
            j = i
            for c,d in zip(costs, durations):
                while j < n and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, helper(j)+c)
            return ans
            
        return helper(0)
