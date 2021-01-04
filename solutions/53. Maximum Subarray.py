class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ### Failed attempt - time exceeded
#         temp = max(nums)
        
#         for i in range(1, len(nums)): #length of subarray
#             j = 0
#             while i + j < len(nums):
#                 temp = max(sum(nums[j:j+i+1]), temp)
#                 j += 1
                
#         return temp
​
​
        ### Soln 1 - greedy algorithm
        cur_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum
