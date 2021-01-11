class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums)
        
        nums[2] += nums[0]
        
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
        
        return max(nums)
                
        
