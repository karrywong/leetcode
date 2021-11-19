class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #first attempt, prefix sum + sliding window
        cur_sum, ans = 0, float('inf')
        n, i, j = len(nums), 0,0
        while i < n and cur_sum+nums[i] < target:
            cur_sum += nums[i] 
            i += 1
        #cur_sum + nums[i] >= target
        while i < n:
            cur_sum += nums[i]
            while j < n and cur_sum - nums[j] >= target: #sliding window
                cur_sum -= nums[j]
                j += 1
            ans = min(ans, i-j+1)
            i += 1    
        return 0 if ans == float('inf') else ans
            
