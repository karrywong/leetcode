class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Leetcode, time O(N), space O(1)
        S = sum(nums)
        cur_sum = 0
        for idx, num in enumerate(nums):
            if cur_sum == S - cur_sum - num:
                return idx
            cur_sum += num
        return -1
        
#         # 1st attempt, prefix_sum and suffix_sum, time O(N), space O(N)
#         prefix_sum = [0]*len(nums)
#         prefix_sum[0] = nums[0]
#         suffix_sum = [0]*len(nums)
#         suffix_sum[-1] = nums[-1]
        
#         for i in range(1,len(nums)):
#             prefix_sum[i] = prefix_sum[i-1] + nums[i]
#             suffix_sum[~i] = suffix_sum[~i+1] + nums[~i]
        
#         for i in range(len(nums)):
#             if prefix_sum[i] == suffix_sum[i]:
#                 return i
#         return -1
