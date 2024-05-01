class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # time O(N), N=len(nums), space O(1)
        target = sum(nums) - x
        left = cur_sum = 0 
        ans = -1
        
        for right in range(len(nums)):
            cur_sum += nums[right]
            
            while cur_sum > target and left <= right:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                ans = max(ans, right-left+1)
        return len(nums) - ans if ans > -1 else ans
    
#         # prefix sum, time O(N), N=len(nums), space O(N)
#         # refer to the 325. Maximum Size Subarray Sum Equals k
#         target = sum(nums) - x
#         if target == 0: return len(nums)
#         seen = {}
#         cur_sum = ans = 0
        
#         for i, num in enumerate(nums):
#             cur_sum += num
#             if cur_sum == target:
#                 ans = i+1
#             if cur_sum-target in seen:
#                 ans = max(ans, i-seen[cur_sum-target])
#             if cur_sum not in seen:
#                 seen[cur_sum] = i
#         return len(nums)-ans if ans > 0 else -1
    
# Testing 
# nums = [1,1,4,2,3], x = 5 -> total_sum = 11 -> target = 6
# 
