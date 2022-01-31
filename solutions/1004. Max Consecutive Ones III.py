class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
#         #First attempt inspired by sliding window in 487. Max Consecutive Ones II
#         #Time O(N), space O(1)
#         left, right = 0, 0
#         count, ans = 0, 0 
#         while right < len(nums):
#             if nums[right] == 0:
#                 count += 1
            
#             while count > k: 
#                 if nums[left] == 0:
#                     count -= 1
#                 left += 1
            
#             ans = max(ans, right-left+1)
#             right += 1
            
#         return ans
    
        ### Old attempts
        ### Soln 2 - sliding window O(n), optimized from LeetCode solution
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of K.
            # Since K is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative K denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase K.
                k += 1 - nums[left]
                left += 1
        return right - left + 1
        
        ### Soln 3 - from discussion by bobroberts454
        # sol, s, q = 0, -1, []
        # for ix, a in enumerate(A):
        #     if a == 0:
        #         q.append(ix)
        #     if len(q) > K:
        #         s = q.pop(0)
        #     sol = max(sol, ix - s)        
        # return sol     
