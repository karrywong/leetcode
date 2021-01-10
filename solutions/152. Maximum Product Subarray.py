class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ### Soln 2 - Dynamic Programming, keeping track of max_val and min_val
        res = nums[0]
        max_val = nums[0]
        min_val = nums[0]
        
        for i in range(1,len(nums)):
            max_temp = max_val * nums[i]
            min_temp = min_val * nums[i]
            
            max_val = max(nums[i], max_temp, min_temp)
            min_val = min(nums[i], max_temp, min_temp)
​
            res = max(max_val, min_val, res)
        return res
​
