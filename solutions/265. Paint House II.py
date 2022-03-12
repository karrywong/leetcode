class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
#         #Almost identical to 256. Paint House
#         #Top-down DP with recursion w memo, time O(n*k^2), space O(n)
#         memo = {} #(house, color)
#         def paint_house(house:int, color:int) -> int:
#             if (house, color) in memo:
#                 return memo[(house, color)]
            
#             if house == len(costs) - 1:
#                 return costs[house][color]
            
#             temp = float('inf')
#             for j in range(len(costs[0])):
#                 if j != color:
#                     temp = min(temp, paint_house(house+1, j))
#             memo[(house, color)] = costs[house][color] + temp
#             return memo[(house, color)]
        
#         ans = float('inf')
#         for j in range(len(costs[0])):
#             ans = min(ans, paint_house(0,j))
#         return ans
        
        #DP with optimized space, dp[i][j]: minimal cost of painting the ith house with jth color
        #Time: O(n*k), space: O(k)
        #Follow-up: can be further optimized to Time: O(n*k), space O(1)
        dp_cur = costs[0]
        for i in range(1,len(costs)):
            dp_prev = dp_cur[:]
            min_color = second_min_color = None
            min_cost = second_min_cost = float('inf')
            
            for j, cost in enumerate(dp_prev):
                if cost < min_cost:
                    second_min_color, min_color = min_color, j
                    second_min_cost, min_cost = min_cost, cost
                elif cost < second_min_cost:
                    second_min_color = j
                    second_min_cost = cost
            
            for j in range(len(dp_cur)):
                if j != min_color:
                    dp_cur[j] = costs[i][j] + min_cost
                else:
                    dp_cur[j] = costs[i][j] + second_min_cost
        return min(dp_cur)
        
        # #DP, dp[i][j]: minimal cost of painting the ith house with jth color
        # #Time: O(n*k^2), space: O(k)
        # dp_cur = costs[0]
        # for i in range(1,len(costs)):
        #     dp_prev = dp_cur[:]
        #     for j in range(len(dp_cur)):
        #         dp_cur[j] = costs[i][j] + min(dp_prev[:j] + dp_prev[j+1:])
        # return min(dp_cur)
