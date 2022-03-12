class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #recursion w memo, time O(N), space O(N)
        memo = {} #(house, color)
        def paint_house(house: int, color: int) -> int:
            if (house, color) in memo:
                return memo[(house, color)]
            
            if house == len(costs)-1:
                return costs[house][color]
            
            cost = costs[house][color]
            if color == 0:
                cost += min(paint_house(house+1, 1), paint_house(house+1, 2))
            elif color == 1:
                cost += min(paint_house(house+1, 0), paint_house(house+1, 2))
            else:
                cost += min(paint_house(house+1, 0), paint_house(house+1, 1))
            memo[(house, color)] = cost
            return cost
        
        return min(paint_house(0,0), paint_house(0,1), paint_house(0,2))
                    
        # #DP soln, time O(len(costs)), space O(1)
        # dp = costs[0]
        # for i in range(1, len(costs)):
        #     dp[0], dp[1], dp[2] = costs[i][0] + min(dp[1], dp[2]), costs[i][1] + min(dp[0], dp[2]), costs[i][2] + min(dp[0], dp[1])
        # return min(dp)
