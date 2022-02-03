class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #top-down DP, similalr to recursion w/ memoization
        # @lru_cache(maxsize=None)
        # def minimum_cost(i):
        #     if i <= 1:
        #         return 0
        #     down_one = cost[i-1] + minimum_cost(i-1)
        #     down_two = cost[i-2] + minimum_cost(i-2)
        #     return min(down_one, down_two)
        # return minimum_cost(len(cost))
        
        #Alternative soln 0 - DP, time O(N), space O(1)
        down_one = down_two = 0
        for i in range(2, len(cost)+1):
            down_one, down_two = min(down_one+cost[i-1], down_two+cost[i-2]), down_one
        return down_one
        
        # #soln 0 - dynamic programming, time O(N), space O(1) in-place
        # for i in range(2,len(cost)):
        #     cost[i] += min(cost[i-2], cost[i-1])
        # return min(cost[-2], cost[-1])
