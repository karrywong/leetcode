class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        #First attempt using DP w/ space optimized, time O(N), space (1)
        #dp = [0] * len(nums)
        cur_sum = nums[0]
        cur_sq = dp = nums[0] * nums[0]
        
        for i in range(1, len(nums)):
            val = nums[i] * nums[i]
            #update cur_sq - either perform square or not
            cur_sq = max(val, cur_sum+val, cur_sq+nums[i])
            #update cur_sum from Kadane's algorithm
            cur_sum = max(nums[i], cur_sum+nums[i])            
            dp = max(dp, cur_sq)
            
        return dp
