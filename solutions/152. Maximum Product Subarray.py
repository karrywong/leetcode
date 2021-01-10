class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ### Soln 2 - Dynamic Programming O(n), keeping track of max_val and min_val
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
        ### Soln 1 - brute force, time exceeded
#         if len(nums) == 0 : 
#             return 0
#         else: 
#             res = nums[0]
        
#         for i in range(len(nums)):
#             accu = 1 
#             for j in range(i, len(nums)):
#                 accu = accu * nums[j]
#                 res = max(res, accu)
#         return res
