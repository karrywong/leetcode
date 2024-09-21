class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,7,9,3,1,100]
        # [2,7,11,10,12,111]
        
        # time O(N), space O(1)
        rob, not_rob = 0,0
        not_rob_prev = 0
        for num in nums:
            not_rob_prev = not_rob
            not_rob = rob
            rob = max(not_rob_prev+num, not_rob)
        return max(rob, not_rob)
            
#         # time O(N), space O(N)
#         if len(nums) == 1:
#             return nums[0]
#         elif len(nums) == 2:
#             return max(nums)
        
#         rob_gain = nums
#         rob_gain[2] += rob_gain[0]
        
#         for i in range(3, len(nums)):
#             rob_gain[i] += max(rob_gain[i-2], rob_gain[i-3])
            
#         return max(rob_gain[-1], rob_gain[-2])
        
        
