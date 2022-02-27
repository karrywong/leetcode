class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:        
        ## Soln 2 - sliding window O(n)
        left, right = 0, 0
        count, ans = 0, 0
        
        while right < len(nums):
            if nums[right] == 0: count += 1
            
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
                
            ans = max(ans, right - left + 1)
            right += 1
        return ans
​
#         #First attempt, straightforward counting, time O(N), space O(1)
#         count1 = 0 #count consecutive ones
#         i = 0
        
#         while i < len(nums) and nums[i] != 0:
#             count1 += 1
#             i += 1
#         if i == len(nums): #entire array is ones
#             return len(nums)
        
#         count2 = 0
#         ans = 0
#         for j in range(i+1, len(nums)):
#             if nums[j] == 1:
#                 count2 += 1
#             else:
#                 ans = max(ans, count1+count2+1)
#                 count1 = count2 #update last seen consecutive ones
#                 count2 = 0
        
#         return max(ans, count1+count2+1)
    
        ### Old attempts
