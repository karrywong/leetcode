class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ### Problem restatement: Given a binary array, find the maximum number of consecutive 1s in this array, allowing at most one 0 within an otherwise consecutive run of 1s
        
        ### Soln 1 - brute force O(n^2), time exceeded
        # res = 0
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i, len(nums)):
        #         if count == 2:
        #             break
        #         if nums[j] == 0:
        #             count += 1
        #         if count <= 1: 
        #             res = max(res, j - i + 1)
        # return res
        
        
        ### Soln 2 - sliding window O(n)
#         left = 0
#         right = 0
#         count = 0
#         res = 0
        
#         while right < len(nums):
#             if nums[right] == 0: count += 1
            
#             while count == 2:
#                 if nums[left] == 0:
#                     count -= 1
#                 left += 1
                
#             res = max(res, right - left + 1)
#             right += 1
#         return res
​
        ### Soln 3 - fast and elegant solution from discussion by redSand
        k = result = 0
        prev_zero_seen = -1
        for i, num in enumerate(nums):
            if num == 0:
                result = max(result, i - k)
                k = prev_zero_seen + 1
                prev_zero_seen = i
        
        return max(result, len(nums) - k)
