class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        #Soln 3 - DP, compute effective score, equivalent to recursion
        #Time O(N^2), space O(N^2)
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            for j in range(i, len(nums)):
                if i==j:
                    dp[i][j] = nums[i]
                else:
                    a = nums[i] - dp[i+1][j]
                    b = nums[j] - dp[i][j-1]
                    dp[i][j] = max(a,b)
        # print(dp)
        return dp[0][-1] >= 0
        
        # #Soln 2 - LeetCode MinMax strategy, recursive optimized
        # #Time O(N^2), space O(N^2)
        # memo = {}
        # def gain(i,j, nums): 
        #     if i == j:
        #         return nums[i]
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     a = nums[i] - gain(i+1,j,  nums)
        #     b = nums[j] - gain(i,  j-1,nums)
        #     memo[(i,j)] = max(a,b)
        #     return memo[(i,j)]
        # return gain(0,len(nums)-1,nums) >= 0
        
#         #Soln 1 - LeetCode MinMax strategy, recursive
#         #Time O(2**N), space O(N)
#         def gain(i,j, nums, turn): #1:player 1, -1:player 2
#             if i == j:
#                 return turn * nums[i]
#             a = turn * nums[i] + gain(i+1,j, nums, -turn)
#             b = turn * nums[j] + gain(i,j-1, nums, -turn)
#             if turn == 1:
#                 return max(a,b)
#             else:
#                 return min(a,b)
#         return gain(0, len(nums)-1, nums, 1) >= 0
