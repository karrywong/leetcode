class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        k = -1 
        j = 0 # last seen 0 position
        cnt_zero = 0
        ans = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt_zero += 1
                if cnt_zero > 1:
                    k = j
                j = i
            ans = max(ans, i-k)
        return ans
    
    #  (i, k, j, ans)
    # [1,0,1,1,0] 
    # (0, -1, 0, 1) -> (1, -1, 1, 2) -> (2,-1,1,3) -> (3,-1,1,4) -> (4,1,4,4)
    
    # [1,0,1,1,0,1,1,1,1,1]
    # ans = 8
    
    # [1,0,1,1,0,1]
    # (0,-1,0,1) -> (1,-1,0,1) -> ... ->(3,-1,0,4) -> (4,1,4,4) -> (5,1,4,4)
​
# ## Soln 2 - fast and elegant solution from discussion by redSand
#         k = result = 0
#         prev_zero_seen = -1
#         for i, num in enumerate(nums):
#             if num == 0:
#                 result = max(result, i - k)
#                 k = prev_zero_seen + 1
#                 prev_zero_seen = i
        
#         return max(result, len(nums) - k)
    
        ### Old attempts
        ### Soln 1 - brute force O(n^2), time exceeded
        # res = 0
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i, len(nums)):
        #         if count == 2:
