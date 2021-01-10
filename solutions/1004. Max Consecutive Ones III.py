class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ### Soln 1 - sliding window O(n), modified from Max Consecutive Ones II
#         left = right = 0
#         res = count = 0
        
#         while right < len(A):
#             if A[right] == 0: count += 1
            
#             while count == K+1:
#                 if A[left] == 0:
#                     count -= 1
#                 left += 1
            
#             res = max(res, right - left + 1)
#             right += 1
            
#         return res 
​
​
        ### Soln 2 - sliding window O(n), optimized from LeetCode solution
        left = 0
        for right in range(len(A)):
            # If we included a zero in the window we reduce the value of K.
            # Since K is the maximum zeros allowed in a window.
            K -= 1 - A[right]
            # A negative K denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if K < 0:
                # If the left element to be thrown out is zero we increase K.
                K += 1 - A[left]
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
