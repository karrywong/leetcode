class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #soln 2 - Leetcode two pointers, Time O(N), Space O(N)
        l = len(nums)
        ans = [0] * l
        negptr, posptr= 0, l-1
        
        for i in range(l-1, -1, -1):
            if abs(nums[negptr]) < abs(nums[posptr]):
                sq = nums[posptr]
                posptr -= 1
            else:
                sq = nums[negptr]
                negptr += 1
            ans[i] = sq*sq
        return ans
        
#         #soln 1 - too complicated, Time O(N), Space O(N)
#         l = len(nums)
#         ans = [None] * l
#         i = 0
#         k = j = l-1
        
#         while i < len(nums) and nums[i] < 0:
#             while abs(nums[i]) <= nums[j]:
#                 ans[k] = nums[j] * nums[j]
#                 j -= 1
#                 k -= 1
#             ans[k] = nums[i] * nums[i] 
#             k -= 1 
#             i += 1
#         ans[:k+1] = [n*n for n in nums[i:i+k+1]]  
#         return ans
        
        #soln 0 - trivial
        #return sorted([i*i for i in nums])
