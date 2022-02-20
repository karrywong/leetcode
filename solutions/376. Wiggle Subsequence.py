class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        #Soln 3 - LeetCode Greedy, time O(N), space O(1)
        if len(nums) == 1: return 1
        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if (diff < 0 and prev_diff >= 0) or (diff > 0 and prev_diff <= 0):
                count += 1
                prev_diff = diff
        return count 
        
#         #Soln 2 - LeetCode optimized DP, time O(N), space O(1)
#         if len(nums) == 1: return 1
        
#         up = down = 1
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i-1]:
#                 up = down + 1
#             elif nums[i] < nums[i-1]:
#                 down = up + 1
#         return max(up, down)
        
#         #Soln 1 - First attempt DP, Time O(N^2), space O(N)
#         if len(nums) == 1: return 1
​
#         sign = [0]*len(nums) #1 or -1
#         dp = [1]*len(nums)
#         for i in range(1, len(nums)):
#             for j in range(0,i):
#                 if j == 0 and nums[i] != nums[0]:
#                     dp[i] = 2
#                     sign[i] = -1 if nums[i] < nums[0] else 1
#                 elif (nums[i] - nums[j])*sign[j] < 0 and dp[j]+1 > dp[i]:
#                     dp[i] = dp[j]+1
#                     sign[i] =  -1 if nums[i] < nums[j] else 1
#         return max(dp)
